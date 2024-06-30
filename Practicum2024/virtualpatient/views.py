from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm, CreatePatientForm
from .models import Patient
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
    context = {'patients': patients, 'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/select.html', context)

@csrf_exempt
#  @login_required(login_url='login')
def simulate(request, pk):
    patient = Patient.objects.get(pk=pk)
    initial = f"You are a patient named {patient.first_name} {patient.last_name}, {patient.age} years old. You are visiting for a consultation. Your details are: {patient.description}. Your symptoms are: {patient.symptoms}. Use a tone described in the patient description and style appropriate for a patient describing their symptoms and medical history.".replace('\r', ' ').replace('\n', ' ').replace('\t',' ')
    initial += f" Your chief and most important complaint is {patient.chief_complaint}."
    initial += f" When asked about the provocation of your pain, you must strictly answer using 'worsen when {patient.provocation}'."
    initial += f" When asked about the quality of your pain, you must strictly answer using 'like {patient.quality}'."
    initial += f" When asked about the region of your pain, you must strictly answer using 'around {patient.region}'."
    initial += f" When asked about the severity of your pain, you must strictly answer using 'rank {patient.severity}'."
    initial += f" When asked about the timing or duration of your pain, you must strictly answer using 'since {patient.timing}'."
    initial += f" Only when you are diagnosed with specifically {patient.illness_to_be_diagnosed}, you must strictly answer 'Thank you for my diagnosis.'."
    initial += f" You must not know of your diagnosis. Strictly speak in 1 sentence at a time."
    initial_prompts = [{"role": "system", "content": initial}]
    context = {'pk':pk, 'image': f"{patient.image}", 'is_teacher': request.user.groups.filter(name='teacher').exists(), 'initial': initial}
    if request.method == 'POST':
        initial_prompts.append({"role": json.loads(request.body).get('role'),"content": json.loads(request.body).get('message')})
        completion = connection.chat.completions.create(model="ft:gpt-3.5-turbo-0125:personal:virtualpatient:9exepl3p", messages=initial_prompts)
        response = completion.choices[0].message.content
        return JsonResponse({"content": response})
    if 'conversation' in request.COOKIES:
        context['conversation'] = (json.loads(request.COOKIES['conversation']))    
    return render(request, 'virtualpatient/simulate.html', context)
    
# @login_required(login_url='login')
def profile(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/profile.html', context)

# @login_required(login_url='login')
def faqs(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/faqs.html', context)
