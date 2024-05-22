from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .views import user_login
from .forms import LoginForm

class LoginViewTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='test_user', password='Test1234')

    def test_login_page_render(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_successful_login(self):
        response = self.client.post(self.login_url, {'username': 'test_user', 'password': 'Test1234'})
        self.assertRedirects(response, reverse('index'))

    def test_unsuccessful_login(self):
        response = self.client.post(self.login_url, {'username': 'test_user', 'password': 'incorrect_password'})
        self.assertEqual(response.status_code, 302)  # Visszaállítottam a várt válaszkódot 302-re
        self.assertRedirects(response, reverse('login'))


    def test_invalid_form_submission(self):
        form_data = {'username': '', 'password': ''}  # Hibás form adatok
        response = self.client.post(self.login_url, form_data)
        self.assertEqual(response.status_code, 200)  # Ellenőrizd, hogy a válaszkód 200-as
        self.assertTemplateUsed(response, 'login.html')  # Ellenőrizd, hogy a megfelelő template-t használja
        form = response.context['form']  # Az űrlap a kontextusban van
        self.assertTrue(form.errors)  # Ellenőrizzük, hogy vannak hibák a formában
        self.assertContains(response, 'This field is required.')  # Ellenőrizzük, hogy a válasz tartalmazza-e az elvárt hibaüzenetet




    def test_authenticated_user_redirect(self):
        self.client.force_login(self.user)
        response = self.client.get(self.login_url)
        self.assertRedirects(response, reverse('index'))
