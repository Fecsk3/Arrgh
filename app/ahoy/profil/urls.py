from django.urls import path
from . import views
urlpatterns = [
    path('profil/', views.profil, name='profil'),
    path('change_data/', views.change_data, name='change_data'),
    path('change_password/', views.change_password, name='change_password'),
]

