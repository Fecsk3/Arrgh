import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

from documents.models import MarkdownFile

markdown_files_data = [
    {
        'name': 'example.md',
        'content': '# This is an example Markdown file.\n\nYou can write your content here...'
    },
    {
        'name': 'test_file.md',
        'content': '## Test file\n\nThis is another Markdown file for testing purposes...'
    }
]
try:
    
    for data in markdown_files_data:
        MarkdownFile.objects.create(name=data['name'], content=data['content'])
except Exception as e:
    print(f'Hiba történt az adatok feltöltésekor: {e}')
else:
    print('Az adatok már feltöltve')
