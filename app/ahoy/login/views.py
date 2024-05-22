from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.messages import constants as messages_constants

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                messages.add_message(request, messages_constants.ERROR, 'Hibás felhasználónév vagy jelszó!')
        else:
            messages.add_message(request, messages_constants.ERROR, 'Hibás adatok vagy felhasználónév!')
    else:
        form = LoginForm()
        if request.user.is_authenticated:
            message = "A bejelentkezés felület nem elérhető bejelentkezett felhasználóknak!"
            messages.add_message(request, messages_constants.INFO, message)
            return redirect(reverse('index'))
    return render(request, 'login.html', {'form': form, 'messages': messages.get_messages(request)})
