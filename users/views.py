from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomUserForm
from django.http import HttpResponse

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserForm()
    
    return render(
        request,
        'register.html',
        {
            "form": form
        }
    )


def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('yaziki:yaizki_programmirovanie')
            #return redirect('/prog_lang/')
    else:
        form = AuthenticationForm()
    
    return render(
        request,
        'login.html',
        {
            "form": form
        }
    )


def auth_logout_view(request):
    logout(request)
    return redirect('/login/')



