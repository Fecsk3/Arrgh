import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from kanban.models import Board, Column, Card
from index.models import Team

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample data for Kanban board'

    def add_arguments(self, parser):
        parser.add_argument('team_id', type=int, help='Team id for which to create the board')

    def handle(self, *args, **kwargs):
        teams_id = kwargs['team_id']

        try:
            team = Team.objects.get(teams_id=teams_id)
        except Team.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Team with ID {teams_id} does not exist."))
            return

        board = Board.objects.create(title='Sample Board', created_by=team)

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

# python manage.py seed_kanban team_id