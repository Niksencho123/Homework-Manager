from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from datetime import date, timedelta
from assignments.models import Assignment

# Create your views here.
def register(request):
    if request.method == "POST":
        registerForm = UserRegistrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            username = registerForm.cleaned_data.get('username')
            messages.success(request, "Профилът беше добавен!")
            return redirect('assignments-success')
    else:
        registerForm = UserRegistrationForm()
    return render(request, 'users/register.html', {"form": registerForm, 'StylesFiles': "styles/register.css"})