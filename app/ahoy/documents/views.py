from django.shortcuts import render
from django.http import HttpResponse
from .models import MarkdownFile

def documents_markdown_files_list(request):
    markdown_files = MarkdownFile.objects.all()
    return render(request, 'documents.html', {'markdown_files': markdown_files})

def download_markdown_file(request, file_id):
    markdown_file = MarkdownFile.objects.get(pk=file_id)
    response = HttpResponse(markdown_file.content, content_type='text/markdown')
    response['Content-Disposition'] = f'attachment; filename="{markdown_file.name}"'
    return response