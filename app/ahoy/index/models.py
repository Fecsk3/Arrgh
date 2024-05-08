from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    teams_id = models.AutoField(primary_key=True)
    senior = models.ForeignKey(User, on_delete=models.CASCADE)
    directory = models.CharField(max_length=100, null=True)
    project_title = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'Team {self.teams_id}'

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.team.teams_id}'
