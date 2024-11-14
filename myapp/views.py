from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    return render(request, 'myapp/login.html')


def register(request):
    return render(request, 'myapp/register.html')

def adminDashboard(request):
    return render(request, 'myapp/admin/dashboard.html')