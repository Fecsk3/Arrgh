import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

from kanban.models import Board, Title, Task  # Import your models

board_data = {
    'board_name': 'Kanban',
    'titles': [
        {
            'title_name': 'Teendő',
            'tasks': [
                {'task_name': 'Task 1.1', 'description': 'Description for Task 1.1'},
                {'task_name': 'Task 1.2', 'description': 'Description for Task 1.2'},
                {'task_name': 'Task 1.3', 'description': 'Description for Task 1.3'},
            ]
        },
        {
            'title_name': 'Folyamatban',
            'tasks': [
                {'task_name': 'Task 2.2', 'description': 'Description for Task 2.2'},
                {'task_name': 'Task 2.3', 'description': 'Description for Task 2.3'},
                {'task_name': 'Task 2.1', 'description': 'Description for Task 2.1'},
            ]
        },
        {
            'title_name': 'Ellenőrzés',
            'tasks': [
                {'task_name': 'Task 3.1', 'description': 'Description for Task 3.1'},
                {'task_name': 'Task 3.2', 'description': 'Description for Task 3.2'},
                {'task_name': 'Task 3.3', 'description': 'Description for Task 3.3'},
            ]
        },
        {
            'title_name': 'Teszt',
            'tasks': [
                {'task_name': 'Task 4.1', 'description': 'Description for Task 4.1'},
                {'task_name': 'Task 4.2', 'description': 'Description for Task 4.2'},
                {'task_name': 'Task 4.3', 'description': 'Description for Task 4.3'},
            ]
        },
        {
            'title_name': 'Kész',
            'tasks': [
                {'task_name': 'Task 5.1', 'description': 'Description for Task 5.1'},
                {'task_name': 'Task 5.2', 'description': 'Description for Task 5.2'},
                {'task_name': 'Task 5.3', 'description': 'Description for Task 5.3'},
            ]
        }
    ]
}

try:
    board = Board.objects.create(board_name=board_data['board_name'])
    for title_data in board_data['titles']:
        title = Title.objects.create(title_name=title_data['title_name'], board_id=board)
        for task_data in title_data['tasks']:
            Task.objects.create(task_name=task_data['task_name'], description=task_data['description'], title_id=title, board_id=board)
except Exception as e:
    print(f'Hiba történt az adatok feltöltésekor: {e}')
else:
    print('Az adatok már feltöltve')
