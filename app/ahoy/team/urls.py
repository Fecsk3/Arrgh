from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team, name='team'),
    path('add_member/', views.add_member, name='add_member'),
    path('finish_team_creation/', views.finish_team_creation, name='finish_team_creation'),
    path('delete_teams/', views.delete_teams_view, name='delete_teams'),  
]
