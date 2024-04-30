




from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate

# Create your views here.

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # check if user exists
            if User.objects.filter(email=user.email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            #check if passwords match
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                user.set_password(password1)
                user.is_active = False
                user.save()
            messages.success(request, 'Account created successfully. Please check your email to activate your account.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        form = UserRegistrationForm()
        context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')


