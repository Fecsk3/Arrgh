from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from index.models import Team, TeamMember

class TeamViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='Admin1234')
        self.client.login(username='admin', password='Admin1234')

    def test_add_member_view(self):
        team = Team.objects.create(senior=self.superuser)
        user = User.objects.create_user(username='test_user', password='Test1234')
        data = {'team_id': team.teams_id, 'user_id': user.id}
        response = self.client.post(reverse('add_member'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TeamMember.objects.count(), 1)

    def test_finish_team_creation_view(self):
        # Create some users
        users = [User.objects.create_user(username=f'user_{i}', password='Test1234') for i in range(1, 6)]
        team = Team.objects.create(senior=self.superuser)
        selected_users = [str(user.id) for user in users[:3]]  # Selecting first 3 users
        data = {'selected_users': selected_users}
        response = self.client.post(reverse('finish_team_creation'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(TeamMember.objects.count(), 3)  # Three members should be added to the team

if __name__ == '__main__':
    unittest.main()
