from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .views import kanban, create_card, move_card, remove_card, edit_card, get_card_color
from .models import Board, Column, Card
from index.models import Team

class KanbanViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_kanban_view_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('kanban'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kanban.html')

    def test_kanban_view_unauthenticated_user(self):
        response = self.client.get(reverse('kanban'))
        self.assertEqual(response.status_code, 302)

    def test_create_card_authenticated_user(self):
        self.client.force_login(self.user)
        team = Team.objects.create(senior=self.user)
        board = Board.objects.create(title='Test Board', created_by=team)
        column = Column.objects.create(title='Test Column', order=0, board=board)
        response = self.client.post(reverse('create_card', args=[column.pk]), {'title': 'Test Card', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Card.objects.filter(title='Test Card').exists())

    def test_move_card_authenticated_user(self):
        self.client.force_login(self.user)
        team = Team.objects.create(senior=self.user)
        board = Board.objects.create(title='Test Board', created_by=team)
        column1 = Column.objects.create(title='Test Column 1', order=0, board=board)
        column2 = Column.objects.create(title='Test Column 2', order=1, board=board)
        card = Card.objects.create(title='Test Card', description='Test Description', column=column1)
        response = self.client.post(reverse('move_card', args=[card.pk, column2.pk]))
        self.assertEqual(response.status_code, 200)
        card.refresh_from_db()
        self.assertEqual(card.column, column2)

    def test_remove_card_authenticated_user(self):
        self.client.force_login(self.user)
        team = Team.objects.create(senior=self.user)
        board = Board.objects.create(title='Test Board', created_by=team)
        column = Column.objects.create(title='Test Column', order=0, board=board)
        card = Card.objects.create(title='Test Card', description='Test Description', column=column)
        response = self.client.post(reverse('remove_card', args=[card.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Card.objects.filter(title='Test Card').exists())

    def test_edit_card_authenticated_user(self):
        self.client.force_login(self.user)
        team = Team.objects.create(senior=self.user)
        board = Board.objects.create(title='Test Board', created_by=team)
        column = Column.objects.create(title='Test Column', order=0, board=board)
        card = Card.objects.create(title='Test Card', description='Test Description', column=column)
        response = self.client.post(reverse('edit_card', args=[card.pk]), {'title': 'Updated Title', 'description': 'Updated Description', 'color': '#FFFFFF'})
        self.assertEqual(response.status_code, 302)
        card.refresh_from_db()
        self.assertEqual(card.title, 'Updated Title')
        self.assertEqual(card.description, 'Updated Description')
        self.assertEqual(card.color, '#FFFFFF')

    def test_get_card_color_authenticated_user(self):
        self.client.force_login(self.user)
        team = Team.objects.create(senior=self.user)
        board = Board.objects.create(title='Test Board', created_by=team)
        column = Column.objects.create(title='Test Column', order=0, board=board)
        card = Card.objects.create(title='Test Card', description='Test Description', column=column, color='#FFFFFF')
        response = self.client.get(reverse('get_card_color', args=[card.pk]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['color'], '#FFFFFF')