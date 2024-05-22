from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from index.models import TeamMember, Team

@login_required(redirect_field_name="bejelentkezes_szukseges")
def index(request):
    message = request.GET.get('message', None)
    if message:
        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html')

@login_required(redirect_field_name="bejelentkezes_szukseges")
def logout_view(request):
    logout(request)
    return redirect('login')


def get_superuser_table_data(request):
    teams = Team.objects.all()
    data = []

    for team in teams:
        # Senior username
        senior_username = team.senior.username if team.senior else ''

        # Team members' usernames
        member_usernames = [member.user.username for member in TeamMember.objects.filter(team=team)]

        # Append data to list
        data.append({'team_id': team.teams_id, 'senior': senior_username, 'members': ', '.join(member_usernames)})

    print(data)  # Kiírjuk a data változó tartalmát a terminálra

    return JsonResponse({'data': data})

def get_staff_table_data(request):
    user_id = request.user.id
    teams = Team.objects.filter(senior_id=user_id)
    data = []

    for team in teams:
        member_usernames = [member.user.username for member in TeamMember.objects.filter(team=team)]
        data.append({'team_id': team.teams_id, 'members': ', '.join(member_usernames)})

    print(data) 

    return JsonResponse({'data': data})
