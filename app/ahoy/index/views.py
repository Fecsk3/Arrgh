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



""" 
@login_required
def get_superuser_table_data(request):
    # Lekérdezi az összes csapatot (teams_id)
    teams = Team.objects.all()

    data = []
    for team in teams:
        # Az adott csapat (teams_id) id-ja
        team_id = team.teams_id
        
        # A csapat seniorjának felhasználóneve
        senior_user = User.objects.get(id=team.senior_id)  # Feltételezve, hogy van 'senior_id' mező a Team modelled
        senior_username = senior_user.username

        # A csapat tagjainak felhasználónevei
        members = TeamMember.objects.filter(team_id=team_id)
        member_usernames = [User.objects.get(id=member.user_id).username for member in members]

        # Táblázat adatok hozzáadása
        data.append({
            'team_id': team_id,
            'senior': senior_username,
            'members': ', '.join(member_usernames)
        })

    return JsonResponse({'data': data})
 """