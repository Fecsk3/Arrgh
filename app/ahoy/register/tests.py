from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import SignUpForm

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.user_data = {
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'Test1234!',
            'password2': 'Test1234!'
        }

    def test_register_page_render(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_successful_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirect to login page upon successful registration

    def test_existing_email_registration(self):
        # Create a user with the same email as in user_data
        User.objects.create_user(username='existing_user', email=self.user_data['email'])
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 200)  # Stay on registration page and display error message

    def test_invalid_form_submission(self):
        # Submit an empty form
        response = self.client.post(self.register_url, {})
        self.assertEqual(response.status_code, 200)  # Stay on registration page and display form errors

        # Submit a form with invalid data
        invalid_data = {
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid_email',  # Invalid email format
            'password1': 'password',  # Password too short
            'password2': 'password'
        }
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)  # Stay on registration page and display form errors
