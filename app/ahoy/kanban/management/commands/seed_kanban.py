import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from kanban.models import Board, Column, Card

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample data for Kanban board'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the user to create the board')

    def handle(self, *args, **kwargs):
        username = kwargs['username']

        user = User.objects.get(username=username)

        board = Board.objects.create(title='Sample Board', created_by=user)

        columns = ['To Do', 'In Progress', 'Review', 'Testing', 'Done']

        for order, title in enumerate(columns):
            column = Column.objects.create(title=title, board=board, order=order)
            
            for _ in range(random.randint(3, 5)):
                Card.objects.create(
                    title=fake.catch_phrase(),
                    description=fake.text(),
                    column=column,
                    order=column.cards.count()
                )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))

# python manage.py seed_kanban myusername
