from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.superuser_messages_view, name='messages'),
    path('sendmessage/', views.send_message, name='send_message'),
    path('delete-messages/', views.delete_messages, name='delete_messages'), 
]
