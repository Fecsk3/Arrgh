from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SeniorSelectionForm, TeamCreationForm
from index.models import Team, TeamMember
from django.http import JsonResponse

@login_required
def team(request):
    if not request.user.is_superuser:
        return redirect('index')

    show_senior_selection = True
    selected_senior_username = None

    if request.method == 'POST':
        if 'select_senior' in request.POST:
            form = SeniorSelectionForm(request.POST)
            if form.is_valid():
                selected_senior = form.cleaned_data['senior']
                # Csapat létrehozása a kiválasztott senior felhasználóval
                team = Team.objects.create(senior=selected_senior)
                selected_senior_username = selected_senior.username
                show_senior_selection = False

    # Szűrjük ki azokat a felhasználókat, akik nem 'is_staff', nem 'is_superuser' és nem szerepelnek a TeamMember táblában
    eligible_users = User.objects.filter(is_staff=False, is_superuser=False).exclude(id__in=TeamMember.objects.values_list('user_id', flat=True))

    senior_form = SeniorSelectionForm()
    return render(request, 'team.html', {
        'senior_form': senior_form,
        'show_senior_selection': show_senior_selection,
        'selected_senior_username': selected_senior_username,
        'eligible_users': eligible_users,  # Adjuk át a template-nek az engedélyezett felhasználók listáját
    })


def add_member(request):
    if request.method == 'POST':
        team_id = request.POST.get('team_id')
        user_id = request.POST.get('user_id')
        if TeamMember.objects.filter(team_id=team_id).count() < 4:
            TeamMember.objects.create(user_id=user_id, team_id=team_id)
            return JsonResponse({'message': 'Sikeres hozzáadás'}, status=200)
        else:
            return JsonResponse({'message': 'A csapat maximális létszáma elérve'}, status=400)
    else:
        return JsonResponse({'message': 'Érvénytelen kérés'}, status=400)

@login_required
def finish_team_creation(request):
    if request.method == 'POST':
        selected_users = request.POST.getlist('selected_users')
        if 1 <= len(selected_users) <= 4:
            # Lekérjük a legutolsó Team rekordot
            latest_team = Team.objects.latest('teams_id')
            team_id = latest_team.teams_id

            # Iterálunk a kiválasztott felhasználókon és beszúrjuk őket a TeamMember táblába
            for user_id in selected_users:
                # Beszúrás a TeamMember táblába az adott csapat (team_id) és felhasználó (user_id) alapján
                TeamMember.objects.create(team_id=team_id, user_id=user_id)
            return redirect('index')

    return redirect('team')  # Ha nincs kiválasztott user vagy a feltételek nem teljesültek, visszatérünk a team oldalra

@login_required
def delete_teams_view(request):
    if request.user.is_superuser:
        Team.objects.all().delete()
        TeamMember.objects.all().delete()
    return redirect('team')  # Minden esetben visszatérünk a team oldalra
