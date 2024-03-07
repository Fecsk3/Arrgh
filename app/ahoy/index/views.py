from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required(redirect_field_name="bejelentkezes_szukseges")
def index(request):
    message = request.GET.get('message', None)
    if (message):
        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def logout_view(request):
    logout(request)
    return redirect('login')