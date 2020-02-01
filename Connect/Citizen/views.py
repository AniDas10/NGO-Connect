from django.shortcuts import render

# Create your views here.
def citizen_login(request):
    return render(request, 'aspiration/login.html')

def citizen_register(request):
    return render(request, 'aspiration/citizen.html')