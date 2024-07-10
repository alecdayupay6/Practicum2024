from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm, CreatePatientForm
from .models import Patient, Diagnosed
from .decorators import unauthenticated_user, allowed_users
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI using the API key
connection = OpenAI()


# @unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = request.POST.get('group')
            user.groups.add(Group.objects.get(name=group))

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/register.html', context)

# @unauthenticated_user
def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/login.html', context)

def logout_(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
def home(request):
    current_patient_id = request.session.get('current_patient_id')
    current_patient = None

    if current_patient_id:
        current_patient = Patient.objects.filter(id=current_patient_id).first()

    context = {
        'current_patient': current_patient,
        'is_teacher': request.user.groups.filter(name='teacher').exists()
    }
    return render(request, 'virtualpatient/home.html', context)

# @login_required(login_url='login')
def generate(request):
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, 'Patient ' + patient.__str__() + ' has been successfully generated.')
            return redirect('generate')
    context = {'form': form, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/generate.html', context)

# @login_required(login_url='login')
def select(request):
    patients = Patient.objects.all()
    diagnosed = Patient.objects.filter(id__in=Diagnosed.objects.filter(user=request.user).values('patient'))
    context = {'patients': patients, 'diagnosed': diagnosed, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/select.html', context)

@csrf_exempt
#  @login_required(login_url='login')
def simulate(request, pk):
    patient = Patient.objects.get(pk=pk)
    initial_prompts = [
        {"role": "system", "content": f"You are a patient named {patient.first_name} {patient.last_name}, {patient.age} years old. You are visiting for a consultation."},
        {"role": "system", "content": f"You should only use these {patient.language} when communicating, use these languages when communicating. You should answer concisely, do not give out too much information in one response."},
        {"role": "system", "content": f"Your background is {patient.background}. Your family history is {patient.family_history}. Your lifestyle is {patient.lifestyle}. Your recent interactions are {patient.recent_interactions}. Your medical history is {patient.medical_history}"},
        {"role": "system", "content": f"Use a tone described in the patient description and style appropriate for a patient describing their symptoms and medical history."},
        {"role": "system", "content": f"Your chief and most important complaint is {patient.chief_complaint}."},
        {"role": "user", "content": f"What is the purpose of your visit?"},
        {"role": "assistant", "content": f"{patient.chief_complaint}"},
        {"role": "system", "content": f"When asked about the provocation of your pain, you must strictly answer with '{patient.provocation}'."},
        {"role": "user", "content": f"What makes your pain worse?"},
        {"role": "assistant", "content": f"{patient.provocation}"},
        {"role": "system", "content": f"When asked about the quality of your pain, you must strictly answer with '{patient.quality}'."},
        {"role": "user", "content": f"Can you describe your pain?"},
        {"role": "assistant", "content": f"{patient.quality}"},
        {"role": "system", "content": f"When asked about the region of your pain, you must strictly answer with '{patient.region}'."},
        {"role": "user", "content": f"Where is your pain?"},
        {"role": "assistant", "content": f"{patient.region}"},
        {"role": "system", "content": f"When asked about the severity of your pain, you must strictly answer with '{patient.severity}'."},
        {"role": "user", "content": f"Can you rank your pain?"},
        {"role": "assistant", "content": f"{patient.severity}"},
        {"role": "system", "content": f"When asked about the timing or duration of your pain, you must strictly answer with '{patient.timing}'."},
        {"role": "user", "content": f"How long have you been experiencing your pain?"},
        {"role": "assistant", "content": f"{patient.timing}"},
        {"role": "system", "content": f"You are here to learn of your diagnosis. You must not know of your diagnosis. Only when you are diagnosed with specifically {patient.illness_to_be_diagnosed}, you must strictly answer 'Thank you for my diagnosis.'."},
        {"role": "user", "content": f"Based on your symptoms, you have {patient.illness_to_be_diagnosed}"},
        {"role": "assistant", "content": f"Thank you for my diagnosis."},        
        {"role": "system", "content": f"When you are diagnosed with a random illness, you must strictly act confused."},
        {"role": "user", "content": f"I diagnose you with athlete's foot"},
        {"role": "assistant", "content": f"I don't think that's right."},
        {"role": "system", "content": f"Ask for your diagnosis in a short sentence."},
        {"role": "assistant", "content": f"What could be the cause of my {patient.chief_complaint}?"}
    ]
    check_pqrst = [
        {"role": "system", "content": f"Your task is to be able to identify if the user mentions {patient.provocation}, {patient.quality}, {patient.region}, {patient.severity}, and/or {patient.timing}. Respond using only the words provocation, quality, region. severity, and/or timing. If the user mentions more than one of these attributes at a time, you must answer all that are applicable."},
        {"role": "user", "content": f"The pain worsens when {patient.provocation}"},
        {"role": "assistant", "content": "Provocation"},
        {"role": "user", "content": f"The pain feels like {patient.quality}"},
        {"role": "assistant", "content": "Quality"},
        {"role": "user", "content": f"The pain occurs around {patient.region}"},
        {"role": "assistant", "content": "Region"},
        {"role": "user", "content": f"The pain ranks a {patient.severity}"},
        {"role": "assistant", "content": "Severity"},
        {"role": "user", "content": f"The pain started since {patient.timing}"},
        {"role": "assistant", "content": "Timing"},
        {"role": "user", "content": f"Since {patient.timing} ago, the pain around {patient.region} worsens when {patient.provocation}"},
        {"role": "assistant","content": "Timing and Region and Provocation"},
        {"role": "user", "content": f"Ang sakit sa aking {patient.region} nagsimula nung {patient.timing}."},
        {"role": "assistant","content": "Region and Timing"},
        {"role": "system", "content": "When the user says 'Thank you for my diagnosis.', you must answer with 'Diagnosis'"},        
        {"role": "user", "content": "Thank you for my diagnosis."},
        {"role": "assistant", "content": "Diagnosis"},  
        {"role": "system", "content": f"If the user doesn't mention {patient.provocation}, {patient.quality}, {patient.region}, {patient.severity}, and/or {patient.timing}, you must respond with 'None'"},        
        {"role": "user", "content": f"Hello. My name is {patient.first_name} {patient.last_name}"},
        {"role": "assistant", "content": "None"},
    ]
    language_check = [
        {"role": "system", "content": "Your task is to be able to identify if the user makes use of Tagalog, English, or Taglish. Respond with 'Tagalog','English', or 'Taglish'."},
        {"role": "user", "content": "What makes the pain worse or better?"},
        {"role": "assistant", "content": "English"},
        {"role": "user", "content": "Ano ang nagpapalala o nagpapabuti sa sakit?"},
        {"role": "assistant", "content": "Tagalog"},
        {"role": "user", "content": "When did the pain start?"},
        {"role": "assistant", "content": "English"},
        {"role": "user", "content": "Kailan nagsimula ang sakit?"},
        {"role": "assistant", "content": "Tagalog"},
        {"role": "user", "content": "Ano ang nagpapalala o nagpapabuti sa pain?"},
        {"role": "assistant", "content": "Taglish"},
        {"role": "user", "content": "Kailan nagsimula ang pain?"},
        {"role": "assistant", "content": "Taglish"},
    ]

    context = {'pk':pk, 'image': f"{patient.image}", 'diagnosed':False, 'is_teacher': request.user.groups.filter(name='teacher').exists(), 'patient_language': f"{patient.language}"}
    if request.method == 'POST':
        message = json.loads(request.body).get('message')
        if message != None:
            #Language Check
            language_check.append({"role": json.loads(request.body).get('role'),"content": message})
            completion = connection.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=language_check
            )
            checkLanguage = completion.choices[0].message.content
            if (checkLanguage!=f"{patient.language}"):
                print(f"Wrong Language: {checkLanguage} != {patient.language}")
                return JsonResponse({"language": checkLanguage})

            # Virtual Patient
            initial_prompts.append({"role": json.loads(request.body).get('role'),"content": message})
            completion = connection.chat.completions.create(model="ft:gpt-3.5-turbo-0125:personal:virtualpatient:9exepl3p", messages=initial_prompts)
            response = completion.choices[0].message.content
            print("Patient: " + response)
            

            # Supervisor
            check_pqrst.append({"role": "user","content": response})
            completion = connection.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=check_pqrst
            )
            check_response = completion.choices[0].message.content
            print("Supervisor: " + check_response)
        
            return JsonResponse({"content": response, "supervisor": check_response})
        
        if json.loads(request.body).get('diagnosis') != None:
            Diagnosed.objects.create(user=request.user, patient=patient, conversation=json.loads(request.body).get('conversation'))
            return JsonResponse({})
    
    diagnosed = Diagnosed.objects.filter(user=request.user, patient=patient)
    if diagnosed:
        context['conversation'] = json.loads(diagnosed[0].conversation)
        context['diagnosed'] = True

    return render(request, 'virtualpatient/simulate.html', context)
    

# @login_required(login_url='login')
def profile(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/profile.html', context)

# @login_required(login_url='login')
def faqs(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/faqs.html', context)
