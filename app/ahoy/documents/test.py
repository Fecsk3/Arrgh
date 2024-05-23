from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from index.models import Team, TeamMember
import os

class DocumentViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser('superuser', 'superuser@example.com', 'password')
        self.staff_user = User.objects.create_user('staffuser', 'staffuser@example.com', 'password', is_staff=True)
        self.regular_user = User.objects.create_user('regularuser', 'regularuser@example.com', 'password')
        self.team = Team.objects.create(senior=self.staff_user, directory='/tmp', project_title='Test Project')
        TeamMember.objects.create(user=self.regular_user, team=self.team)
    
    def login(self, user):
        self.client.login(username=user.username, password='password')

    def test_documents_view_superuser(self):
        self.login(self.superuser)
        response = self.client.get(reverse('documents_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.team.project_title)
    
    def test_documents_view_staff_user(self):
        self.login(self.staff_user)
        response = self.client.get(reverse('documents_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.team.project_title)
    
    def test_documents_view_regular_user(self):
        self.login(self.regular_user)
        response = self.client.get(reverse('documents_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.team.project_title)
    
    def test_documents_view_no_teams(self):
        self.login(self.superuser)
        Team.objects.all().delete()
        response = self.client.get(reverse('documents_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nincs még csapat létrehozva.")

    def test_download_markdown_file_superuser(self):
        self.login(self.superuser)
        with open('/tmp/requirements_specification_generated.md', 'w') as f:
            f.write('Test content')
        response = self.client.get(reverse('download_markdown_file', args=['requirements', self.team.teams_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/markdown')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="requirements_specification_generated.md"')
        self.assertEqual(response.content.decode(), 'Test content')
        os.remove('/tmp/requirements_specification_generated.md')
    
    def test_download_markdown_file_not_found(self):
        self.login(self.superuser)
        response = self.client.get(reverse('download_markdown_file', args=['requirements', self.team.teams_id]))
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "A fájl nem található.")

    def test_download_markdown_file_invalid_type(self):
        self.login(self.superuser)
        response = self.client.get(reverse('download_markdown_file', args=['invalid_type', self.team.teams_id]))
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Érvénytelen fájltípus.")

    def test_download_markdown_file_no_directory(self):
        self.login(self.superuser)
        team_without_directory = Team.objects.create(senior=self.staff_user, directory='', project_title='No Directory')
        response = self.client.get(reverse('download_markdown_file', args=['requirements', team_without_directory.teams_id]))
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Nincs fájl elérési útvonal megadva.")