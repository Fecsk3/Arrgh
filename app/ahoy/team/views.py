from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeamCreationForm
from index.models import Team, TeamMember
from django.contrib.auth.models import User

@login_required
def team(request):
    user = request.user

    if user.is_superuser:
        if request.method == 'POST':
            form = TeamCreationForm(request.POST)
            if form.is_valid():
                senior_id = form.cleaned_data['senior'].id
                team = Team.objects.create(senior_id=senior_id)
                members = form.cleaned_data['members']
                for member_id in members:
                    TeamMember.objects.create(user_id=member_id.id, team=team)
                return redirect('team')
        else:
            form = TeamCreationForm()

        context = {
            'form': form
        }
        return render(request, 'team.html', context)

    elif user.is_staff:
        teams = Team.objects.filter(senior_id=user.id)
        team_details = []

        for team_obj in teams:
            team_info = {}
            team_info['team'] = team_obj.teams_id
            team_info['members'] = [member.user.username for member in TeamMember.objects.filter(team=team_obj)]
            team_details.append(team_info)

        context = {
            'team_details': team_details
        }

        return render(request, 'team.html', context)

    else:
        # Non-staff, non-superuser users will see their own teams and members
        team_ids = TeamMember.objects.filter(user=user).values_list('team_id', flat=True)
        teams = Team.objects.filter(teams_id__in=team_ids)

        team_details = []

        for team_obj in teams:
            team_info = {}
            team_info['team'] = team_obj.teams_id
            team_info['members'] = [member.user.username for member in TeamMember.objects.filter(team=team_obj)]
            team_details.append(team_info)

        context = {
            'team_details': team_details
        }

        return render(request, 'team.html', context)
