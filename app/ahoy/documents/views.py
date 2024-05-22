from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from index.models import Team, TeamMember
from django.contrib.auth.models import User

@login_required
def documents_view(request):
    user = request.user

    if user.is_superuser:
        teams = Team.objects.all()
    elif user.is_staff:
        teams = Team.objects.filter(senior=user)
    else:
        team_members = TeamMember.objects.filter(user=user)
        if team_members.exists():
            teams = Team.objects.filter(teams_id__in=team_members.values_list('team_id', flat=True))
        else:
            teams = Team.objects.none()

    if not teams.exists():
        if user.is_superuser:
            message = "Nincs még csapat létrehozva."
        else:
            message = "Nincs még csapatod."
        return render(request, 'documents.html', {'message': message})

    selected_team = None
    if request.method == 'POST':
        team_id = request.POST.get('team_id')
        selected_team = get_object_or_404(Team, teams_id=team_id)
    
    return render(request, 'documents.html', {
        'teams': teams,
        'selected_team': selected_team
    })

@login_required
def download_markdown_file(request, file_type, team_id):
    team = get_object_or_404(Team, teams_id=team_id)
    directory = team.directory
    if not directory:
        return HttpResponse("Nincs fájl elérési útvonal megadva.", status=400)

    file_path_map = {
        'requirements': 'requirements_specification_generated.md',
        'functional': 'functional_specification_generated.md',
        'system': 'system_plan_generated.md'
    }

    if file_type not in file_path_map:
        return HttpResponse("Érvénytelen fájltípus.", status=400)

    file_path = f"{directory}/{file_path_map[file_type]}"
    try:
        with open(file_path, 'r') as file:
            response = HttpResponse(file.read(), content_type='text/markdown')
            response['Content-Disposition'] = f'attachment; filename="{file_path_map[file_type]}"'
            return response
    except FileNotFoundError:
        return HttpResponse("A fájl nem található.", status=404)
