from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TeamCreationForm
from index.models import Team, TeamMember
from django.http import JsonResponse

@login_required
def team(request):
    if not request.user.is_superuser:
        return redirect('index')

    show_senior_selection = True
    show_add_members = False
    can_add_member = False

    if request.method == 'POST':
        if 'select_senior' in request.POST:
            form = TeamCreationForm(request.POST)
            if form.is_valid():
                team = form.save(commit=False)
                team.save()
                team.senior_id = request.POST['senior']
                team.save()
                show_senior_selection = False
                show_add_members = True
                can_add_member = True
        elif 'finish' in request.POST:
            selected_users = request.POST.getlist('selected_users')
            if 1 <= len(selected_users) <= 4:
                team_id = Team.objects.latest('id').id
                for user_id in selected_users:
                    TeamMember.objects.create(user_id=user_id, team_id=team_id)
                return redirect('index')
            else:
                return render(request, 'team.html', {
                    'show_senior_selection': show_senior_selection,
                    'show_add_members': show_add_members,
                    'available_users': User.objects.filter(is_staff=True),
                    'assigned_user_ids': TeamMember.objects.values_list('user_id', flat=True),
                })

    form = TeamCreationForm()
    return render(request, 'team.html', {
        'form': form,
        'show_senior_selection': show_senior_selection,
        'show_add_members': show_add_members,
        'available_users': User.objects.filter(is_staff=True),
        'assigned_user_ids': TeamMember.objects.values_list('user_id', flat=True),
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

def finish_team_creation(request):
    selected_users = request.POST.getlist('selected_users')
    if 1 <= len(selected_users) <= 4:
        team_id = Team.objects.latest('id').id
        for user_id in selected_users:
            TeamMember.objects.create(user_id=user_id, team_id=team_id)
        return redirect('index')
    else:
        return render(request, 'team.html', {
            'show_senior_selection': False,
            'show_add_members': True,
            'available_users': User.objects.filter(is_staff=False, is_superuser=False),
            'assigned_user_ids': TeamMember.objects.values_list('user_id', flat=True),
        })

@login_required
def delete_teams_view(request):
    if request.user.is_superuser:
        Team.objects.all().delete()
        TeamMember.objects.all().delete()
        return redirect('team')  # Visszairányítás a csapatok oldalra
    else:
        # Ha nem superuser, akkor megfelelő kezelés (pl. visszairányítás más oldalra)
        return redirect('index')  # Példa: visszairányítás a főoldalra