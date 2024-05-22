from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('get-superuser-table-data/', views.get_superuser_table_data, name='get_superuser_table_data'),
    path('get_staff_table_data/', views.get_staff_table_data, name='get_staff_table_data'),
    path('logout_view/', views.logout_view, name='logout_view'),
]

