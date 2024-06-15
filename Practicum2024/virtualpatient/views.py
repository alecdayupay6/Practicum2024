from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'virtualpatient/register.html', context)

def login_(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, passowrd=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect.')
        context = {}
        return render(request, 'virtualpatient/login.html', context)

def logout_(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
def home(request):
    return render(request, 'virtualpatient/home.html')

# @login_required(login_url='login')
def generate(request):
    return render(request, 'virtualpatient/generate.html')

# @login_required(login_url='login')
def select(request):
    return render(request, 'virtualpatient/select.html')

# @login_required(login_url='login')
def simulate(request):
    return render(request, 'virtualpatient/simulate.html')

# @login_required(login_url='login')
def profile(request):
    return render(request, 'virtualpatient/profile.html')

# @login_required(login_url='login')
def faqs(request):
    return render(request, 'virtualpatient/faqs.html')
