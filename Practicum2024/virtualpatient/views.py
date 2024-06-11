from django.shortcuts import render

def home(request):
    return render(request, 'virtualpatient/home.html')

def create(request):
    return render(request, 'virtualpatient/create.html')

def checkup(request):
    return render(request, 'virtualpatient/checkup.html')
