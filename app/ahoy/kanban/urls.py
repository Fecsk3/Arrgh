from django.urls import path
from . import views
urlpatterns = [
    path('kanban/', views.kanban, name='kanban'), 
    path('move-card/<int:card_id>/<int:column_id>/', views.move_card, name='move_card'),
    path('create_card/<int:column_id>/', views.create_card, name='create_card'),
    path('remove_card/<int:card_id>/', views.remove_card, name='remove_card'),
    path('edit_card/<int:card_id>/', views.edit_card, name='edit_card'),
    path('get_card_color/<int:card_id>/', views.get_card_color, name='get_card_color'),
]