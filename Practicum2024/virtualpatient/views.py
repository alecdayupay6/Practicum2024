from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
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


@unauthenticated_user
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

@unauthenticated_user
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

@login_required(login_url='login')
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def generate(request):
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            if patient.sex == "Male":
                if patient.age <= 10:   #M0-10
                    patient.image = "images/M0-10.png/"
                elif patient.age <= 20: #M11-20
                    patient.image = "images/M11-20.png/"
                elif patient.age <= 40: #M21-40              
                    patient.image = "images/M21-40.png/"
                elif patient.age <= 60: #M41-60
                    patient.image = "images/M41-60.png/"
                else:                   #M61+
                    patient.image = "images/M61+.png/"
            else:
                if patient.age <= 10:   #F0-10
                    patient.image = "images/F0-10.png/"
                elif patient.age <= 20: #F12-20
                    patient.image = "images/F11-20.png/"
                elif patient.age <= 40: #F21-40              
                    patient.image = "images/F21-40.png/"
                elif patient.age <= 60: #F41-60
                    patient.image = "images/F41-60.png/"
                else:                   #F61+
                    patient.image = "images/F61+.png/"
            patient.save()
            return redirect('select')        
        else:
            messages.error(request, 'Invalid input.')
    context = {'form': form, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/generate.html', context)

@login_required(login_url='login')
def select(request):
    patients = Patient.objects.all()
    by_user = Patient.objects.filter(created_by=request.user)
    filters = [-1, -1, -1, -1, -1]
    if request.method == 'POST':
        filterName = request.POST.get('Name')
        filterAge = request.POST.get('Age')
        filterSex = request.POST.get('Sex')
        filterLanguage = request.POST.get('Language')
        filterTeacher = request.POST.get('Teacher')

        # Filter Name
        if filterName=="A-Z":
            patients = patients.order_by('last_name')
            filters[0] = 0
        elif filterName=="Z-A":
            patients = patients.order_by('last_name').reverse()
            filters[0] = 1

        # Filter Age
        if filterAge=="0-10":
            patients = patients.filter(age__lt=11)
            filters[1] = 0
        elif filterAge=="11-20":
            patients = patients.filter(age__lt=21).filter(age__gt=10)
            filters[1] = 1
        elif filterAge=="21-40":
            patients = patients.filter(age__lt=41).filter(age__gt=20)
            filters[1] = 2
        elif filterAge=="41-60":
            patients = patients.filter(age__lt=61).filter(age__gt=40)
            filters[1] = 3
        elif filterAge=="61+":
            patients = patients.filter(age__gt=60)
            filters[1] = 4

        # Filter Sex
        if filterSex=="Male":
            patients = patients.filter(sex="Male")
            filters[2] = 0
        elif filterSex=="Female":
            patients = patients.filter(sex="Female")
            filters[2] = 1

        # Filter Language
        if filterLanguage=="English":
            patients = patients.filter(language="English")
            filters[3] = 0
        elif filterLanguage=="Taglish":
            patients = patients.filter(language="Taglish")
            filters[3] = 1
        elif filterLanguage=="Tagalog":
            patients = patients.filter(language="Tagalog")
            filters[3] = 2

        # Filter Teacher
        if filterTeacher=="A-Z":
            patients = patients.order_by('created_by')
            filters[4] = 0
        elif filterTeacher=="Z-A":
            patients = patients.order_by('created_by').reverse()
            filters[4] = 1
        elif filterTeacher=="User":
            patients = patients.filter(created_by=request.user)
            filters[4] = 2
        
    diagnosed = Patient.objects.filter(id__in=Diagnosed.objects.filter(user=request.user).values('patient'))
    context = {'patients': patients, 'by_user': by_user, 'diagnosed': diagnosed, 'filters': filters, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/select.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def edit(request, pk):
    patient = Patient.objects.get(pk=pk)
    if patient.created_by != request.user:
        return redirect('select')
    form = CreatePatientForm(instance=patient)
    if request.method == 'POST':
        form = CreatePatientForm(request.POST, instance=patient)
        if form.is_valid():
            if patient.sex == "Male":
                if patient.age <= 10:   #M0-10
                    patient.image = "images/M0-10.png/"
                elif patient.age <= 20: #M11-20
                    patient.image = "images/M11-20.png/"
                elif patient.age <= 40: #M21-40              
                    patient.image = "images/M21-40.png/"
                elif patient.age <= 60: #M41-60
                    patient.image = "images/M41-60.png/"
                else:                   #M61+
                    patient.image = "images/M61+.png/"
            else:
                if patient.age <= 10:   #F0-10
                    patient.image = "images/F0-10.png/"
                elif patient.age <= 20: #F12-20
                    patient.image = "images/F11-20.png/"
                elif patient.age <= 40: #F21-40              
                    patient.image = "images/F21-40.png/"
                elif patient.age <= 60: #F41-60
                    patient.image = "images/F41-60.png/"
                else:                   #F61+
                    patient.image = "images/F61+.png/"
            form.save()
            return redirect('select')
        else:
            messages.error(request, 'Invalid input.')
    context = {'form': form, 'patient': patient, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/edit.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def delete(request, pk):
    patient = Patient.objects.get(pk=pk)
    if patient.created_by != request.user:
        return redirect('select')
    if request.method == 'POST':
        patient.delete()
        return redirect('select')
    context = {'patient': patient, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/delete.html', context)

@csrf_exempt
@login_required(login_url='login')
def simulate(request, pk):
    patient = Patient.objects.get(pk=pk)
    diagnosed = Diagnosed.objects.filter(user=request.user, patient=patient)
    initial_prompts = [
        {"role": "system", "content": f"You are a patient named {patient.first_name} {patient.last_name}, {patient.age} years old. You are visiting for a consultation."},
        {"role": "system", "content": f"You are a patient with the birthday {patient.birthday}"},
        {"role": "system", "content": f"You should only use these {patient.language} when communicating, use these languages when communicating. You should answer concisely, do not give out too much information in one response."},
        {"role": "system", "content": f"Your attending physician is {patient.attending_physician_first_name} {patient.attending_physician_last_name}."},
        {"role": "system", "content": f"You have accurate knowledge for {patient.accuracy}."},
        {"role": "system", "content": f"Your address is {patient.address}"},
        {"role": "system", "content": f"the kind of dwelling you live in is {patient.dwelling_type}. It has {patient.number_of_rooms}, {patient.appliances} with {patient.number_of_household_members} in the household."},
        {"role": "system", "content": f"You are a patient with the birthday {patient.birthday}"},
        {"role": "system", "content": f"Your guardian or parent is {patient.parent_guardian_first_name} {patient.parent_guardian_last_name}."},
        {"role": "system", "content": f"Your annual family income is {patient.annual_family_income}"},
        {"role": "system", "content": f"You informant is {patient.informant_first_name} {patient.informant_last_name}"},
        {"role": "system", "content": f"You are a patient with {patient.reliability} reliability when answering questions."},
        {"role": "system", "content": f"You use {patient.transportation} for transportation."},
        {"role": "system", "content": f"Your landline number is {patient.landline_number} and your phone number is {patient.phone_number}."},
        {"role": "system", "content": f"Your nationality is {patient.nationality} and your religion is {patient.religion}"},
        {"role": "system", "content": f"You are a patient with the birthday {patient.birthday}"},
        {"role": "system", "content": f"Your chief and most important complaint is {patient.chief_complaint}. Your main concerns about the problem is/are {patient.concerns_regarding_problem}."},
        {"role": "user", "content": f"What is the purpose of your visit?"},
        {"role": "assistant", "content": f"{patient.chief_complaint}"},
        {"role": "user", "content": f"Do you have concerns in regards to your problem?"},
        {"role": "assistant", "content": f"{patient.concerns_regarding_problem}"},
        {"role": "system", "content": f"You have had history with this illness for about {patient.history_of_present_illness}."},
        {"role": "user", "content": f"How long have you had this problem?"},
        {"role": "assistant", "content": f"{patient.history_of_present_illness}"},
        {"role": "system", "content": f"The stakeholder is {patient.stakeholder}."},
        {"role": "system", "content": f"Your interest in issue is {patient.interest_in_issue}."}, 
        {"role": "system", "content": f"Your role is {patient.role}."},
        {"role": "system", "content": f"Your influence level of {patient.level_of_influence}."},
        {"role": "system", "content": f"You have had history with this illness for about {patient.history_of_present_illness}."},
        {"role": "system", "content": f"You have pertinent belief/s, such as {patient.pertinent_beliefs}."},
        {"role": "system", "content": f"This is will have a {patient.impact_on_family} impact on your family."},
        {"role": "system", "content": f"Factors in the community like {patient.facilitating_community_factors} facilitate and help you, but {patient.hindering_community_factors} hinder you."},  
        {"role": "system", "content": f"Your illness gives you burdens like {patient.burden_of_illness_community_factors}."},
        {"role": "system", "content": f"{patient.pertinent_legislation_or_policies_community_factors} are pertinent legislations or policies that affect you."},
        {"role": "system", "content": f"You were breastfed till {patient.breastfed_till}."},
        {"role": "system", "content": f"You were given {patient.formula} as a baby."},
        {"role": "system", "content": f"Your current diet is {patient.current_diet}, with {patient.food_allergy} allergy/ies."},
        {"role": "system", "content": f"You were given {patient.formula} as a baby."},
        # {"role": "system", "content": f"Your background is {patient.background}. Your family history is {patient.family_history}. Your lifestyle is {patient.lifestyle}. Your recent interactions are {patient.recent_interactions}. Your medical history is {patient.medical_history}"},
        # {"role": "system", "content": f"Use a tone described in the patient description and style appropriate for a patient describing their symptoms and medical history."},
        # {"role": "system", "content": f"Your chief and most important complaint is {patient.chief_complaint}."},
        # {"role": "user", "content": f"What is the purpose of your visit?"},
        # {"role": "assistant", "content": f"{patient.chief_complaint}"},
        # {"role": "system", "content": f"When asked about the provocation of your pain, you must strictly answer with '{patient.provocation}'."},
        # {"role": "user", "content": f"What makes your pain worse?"},
        # {"role": "assistant", "content": f"{patient.provocation}"},
        # {"role": "system", "content": f"When asked about the quality of your pain, you must strictly answer with '{patient.quality}'."},
        # {"role": "user", "content": f"Can you describe your pain?"},
        # {"role": "assistant", "content": f"{patient.quality}"},
        # {"role": "system", "content": f"When asked about the region of your pain, you must strictly answer with '{patient.region}'."},
        # {"role": "user", "content": f"Where is your pain?"},
        # {"role": "assistant", "content": f"{patient.region}"},
        # {"role": "system", "content": f"When asked about the severity of your pain, you must strictly answer with '{patient.severity}'."},
        # {"role": "user", "content": f"Can you rank your pain?"},
        # {"role": "assistant", "content": f"{patient.severity}"},
        # {"role": "system", "content": f"When asked about the timing or duration of your pain, you must strictly answer with '{patient.timing}'."},
        # {"role": "user", "content": f"How long have you been experiencing your pain?"},
        # {"role": "assistant", "content": f"{patient.timing}"},
        # {"role": "system", "content": f"You are here to learn of your diagnosis. You must not know of your diagnosis. Only when you are diagnosed with specifically {patient.illness_to_be_diagnosed}, you must strictly answer 'Thank you for my diagnosis.'."},
        # {"role": "user", "content": f"Based on your symptoms, you have {patient.illness_to_be_diagnosed}"},
        # {"role": "assistant", "content": f"Thank you for my diagnosis."},        
        # {"role": "system", "content": f"When you are diagnosed with a random illness, you must strictly act confused."},
        # {"role": "user", "content": f"I diagnose you with athlete's foot"},
        # {"role": "assistant", "content": f"I don't think that's right."},
        # {"role": "system", "content": f"Ask for your diagnosis in a short sentence."},
        # {"role": "assistant", "content": f"What could be the cause of my {patient.chief_complaint}?"}
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
            # language_check.append({"role": json.loads(request.body).get('role'),"content": message})
            # completion1 = connection.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=language_check
            # )
            # checkLanguage = completion1.choices[0].message.content
            # if checkLanguage not in patient.language:
            #     if patient.language.lower() != "taglish":
            #         print(f"Wrong Language: {checkLanguage} not in {patient.language}")
            #         return JsonResponse({"language": checkLanguage})

            # Virtual Patient
            initial_prompts.append({"role": json.loads(request.body).get('role'),"content": message})
            completion = connection.chat.completions.create(model="ft:gpt-3.5-turbo-0125:personal:virtualpatientv5:9mKTweFc", messages=initial_prompts)
            response = completion.choices[0].message.content
            print("Patient: " + response)
            

            # Supervisor
            check_pqrst.append({"role": "user","content": response})
            completion = connection.chat.completions.create(
                model="ft:gpt-3.5-turbo-0125:personal:virtualpatientv3:9lwH7vPA",
                messages=check_pqrst
            )
            check_response = completion.choices[0].message.content
            print("Supervisor: " + check_response)
        
            return JsonResponse({"content": response, "supervisor": check_response})
        
        if json.loads(request.body).get('diagnosis') != None:
            conversation = json.loads(request.body).get('conversation')
            if conversation != None:
                Diagnosed.objects.create(user=request.user, patient=patient, conversation=json.loads(request.body).get('conversation'))
            else:
                diagnosed[0].delete()
            return JsonResponse({})
    if diagnosed:
            context['conversation'] = json.loads(diagnosed[0].conversation)
            context['diagnosed'] = True
    return render(request, 'virtualpatient/simulate.html', context)
    

@login_required(login_url='login')
def profile(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/profile.html', context)

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/change_password.html', context)

@login_required(login_url='login')
def faqs(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/faqs.html', context)
