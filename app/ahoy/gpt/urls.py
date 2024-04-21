from django.urls import path
from . import views

urlpatterns = [
    path('gpt/', views.gpt, name='gpt'), 
]
