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

# Configure OpenAI with the API key
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
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
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
def simulate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')

        initial_prompts = [
            {
                "role": "system",
                "content": "You are a 26-year-old man from the Philippine slums. Use Filipino slang to communicate your medical history."
            },
            {
                "role": "user",
                "content": "Sige po, doc. Ready na po ako mag-usap."
            },
            {
                "role": "assistant",
                "content": "Hi, doc. Kamusta po? Ako nga pala si Jun, 26 years old. May mga nararamdaman kasi akong kakaiba lately kaya pumunta ako dito."
            },
            {
                "role": "user",
                "content": message
            }
        ]

        # Send the message to OpenAI's API and receive the response
        completion = connection.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=initial_prompts
        )

        response = completion.choices[0].message.content
        return JsonResponse({"content": response})
    
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/simulate.html', context)
# @login_required(login_url='login')
def profile(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/profile.html', context)

# @login_required(login_url='login')
def faqs(request):
    context = {'is_teacher': request.user.groups.filter(name='teacher').exists()}
    return render(request, 'virtualpatient/faqs.html', context)



