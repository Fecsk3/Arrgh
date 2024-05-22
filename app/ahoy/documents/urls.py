from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.documents_view, name='documents'),
    path('download/<str:file_type>/<int:team_id>/', views.download_markdown_file, name='download_markdown_file'),
]