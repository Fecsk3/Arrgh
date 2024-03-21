from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('change_data/', views.change_data, name='change_data'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout_view/', views.logout_view, name='logout_view'),
]

