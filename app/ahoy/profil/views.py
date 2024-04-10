from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm
import requests
from django.contrib import messages

@login_required(redirect_field_name="bejelentkezes_szukseges")
def profil(request):
    message = request.GET.get('message', None)
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profil')
    else:
        form = UserProfileForm(instance=user)

    if message:
        return render(request, 'profil.html', {'form': form, 'message': message})
    else:
        return render(request, 'profil.html', {'form': form})


@login_required(redirect_field_name="bejelentkezes_szukseges")
def change_data(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profil')
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'change_data.html', {'form': form})

from django.contrib.auth import update_session_auth_hash

@login_required(redirect_field_name="bejelentkezes_szukseges")
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'A jelszó sikeresen megváltozott!')
            return redirect('profil')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})
