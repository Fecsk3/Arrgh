from django.urls import path
from . import views
urlpatterns = [
    path('kanban/', views.kanban, name='kanban'), 
    path('move-card/<int:card_id>/<int:column_id>/', views.move_card, name='move_card'),
]