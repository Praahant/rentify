from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterModelForm
from django.http import HttpResponse

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
            return HttpResponse('email or phone number already exists!!!!')
        user = User(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('property_list')
        else:
            return HttpResponse('Invalid email or password!')

    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')