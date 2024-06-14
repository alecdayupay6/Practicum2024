from django.shortcuts import render

def home(request):
    return render(request, 'virtualpatient/home.html')

def login(request):
    return render(request, 'virtualpatient/login.html')

def register(request):
    return render(request, 'virtualpatient/register.html')

def generate(request):
    return render(request, 'virtualpatient/generate.html')

def select(request):
    return render(request, 'virtualpatient/select.html')

def simulate(request):
    return render(request, 'virtualpatient/simulate.html')

def profile(request):
    return render(request, 'virtualpatient/profile.html')

def faqs(request):
    return render(request, 'virtualpatient/faqs.html')
