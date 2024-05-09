from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.user_list_view, name='messages'),
    path('messages/', views.send_message, name='messages'),
]
