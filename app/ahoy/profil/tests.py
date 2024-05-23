from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from .forms import UserProfileForm, CustomPasswordChangeForm

class UserProfileTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.client.login(username='testuser', password='password')

    def test_profile_view_get(self):
        response = self.client.get(reverse('profil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profil.html')
        self.assertIsInstance(response.context['form'], UserProfileForm)

    def test_profile_view_post_valid(self):
        response = self.client.post(reverse('profil'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.email, 'john.doe@example.com')

    def test_profile_view_post_invalid(self):
        response = self.client.post(reverse('profil'), {
            'first_name': '',
            'last_name': '',
            'email': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profil.html')
        self.assertIsInstance(response.context['form'], UserProfileForm)
        self.assertTrue(response.context['form'].errors)

    def test_change_data_view_get(self):
        response = self.client.get(reverse('change_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_data.html')
        self.assertIsInstance(response.context['form'], UserProfileForm)

    def test_change_data_view_post_valid(self):
        response = self.client.post(reverse('change_data'), {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.first_name, 'Jane')
        self.assertEqual(self.user.last_name, 'Smith')
        self.assertEqual(self.user.email, 'jane.smith@example.com')

    def test_change_data_view_post_invalid(self):
        response = self.client.post(reverse('change_data'), {
            'first_name': '',
            'last_name': '',
            'email': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_data.html')
        self.assertIsInstance(response.context['form'], UserProfileForm)
        self.assertTrue(response.context['form'].errors)

    def test_change_password_view_get(self):
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_password.html')
        self.assertIsInstance(response.context['form'], CustomPasswordChangeForm)

    def test_change_password_view_post_valid(self):
        response = self.client.post(reverse('change_password'), {
            'old_password': 'password',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'A jelszó sikeresen megváltozott!')
        self.assertTrue(self.user.check_password('newpassword123'))

    def test_change_password_view_post_invalid(self):
        response = self.client.post(reverse('change_password'), {
            'old_password': 'password',
            'new_password1': 'newpassword123',
            'new_password2': 'differentpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_password.html')
        self.assertIsInstance(response.context['form'], CustomPasswordChangeForm)
        self.assertTrue(response.context['form'].errors)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("A két jelszó mező nem egyezik" in str(message) for message in messages))
