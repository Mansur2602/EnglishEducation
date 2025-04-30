from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, LoginForm


def home(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')  

            else:
                login_form.add_error(None, 'Неверный логин или пароль.')

    return render(request, 'English_app/main.html', {'form': login_form})




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegistrationForm()

    return render(request, 'English_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 
