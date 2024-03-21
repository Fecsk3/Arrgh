from django.urls import path
from . import views
urlpatterns = [
    path('kanban/', views.kanban, name='kanban'), 
]