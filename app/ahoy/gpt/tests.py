from django.test import TestCase, Client, RequestFactory
from .forms import ProjectForm
from .models import Project
from django.urls import reverse
from django.contrib.auth.models import User
from .views import gpt, generate_gpt_response, description_for_project, load_templates, save_templates_responses

class ProjectFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'title': 'Test Project',
            'goal': 'Create a test project.',
            'target_users': 'Developers',
            'problem_motivation': 'Test problem.',
            'technical_stack': 'Django, React',
            'key_features': 'Feature 1\nFeature 2',
            'deliverables': 'Complete app',
            'timeline': '1 month',
            'additional_info': 'No additional info'
        }
        form = ProjectForm(data=data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        data = {
            'title': '', 
            'goal': 'Create a test project.',
            'target_users': 'Developers',
            'problem_motivation': 'Test problem.',
            'technical_stack': 'Django, React',
            'key_features': 'Feature 1\nFeature 2',
            'deliverables': 'Complete app',
            'timeline': '1 month',
            'additional_info': 'No additional info'
        }
        form = ProjectForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            goal='Create a test project.',
            target_users='Developers',
            problem_motivation='Test problem.',
            technical_stack='Django, React',
            key_features='Feature 1\nFeature 2',
            deliverables='Complete app',
            timeline='1 month',
            additional_info='No additional info'
        )

    def test_project_creation(self):
        self.assertTrue(isinstance(self.project, Project))
        self.assertEqual(self.project.__str__(), self.project.title)

class GptViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.user.save()
    
    def test_gpt_view_get(self):
        request = self.factory.get(reverse('gpt'))
        request.user = self.user

        response = gpt(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form")
    
    def test_description_for_project(self):
        form_data = {
            'title': 'Test Title',
            'goal': 'Test Goal',
            'target_users': 'Test Users',
            'problem_motivation': 'Test Motivation',
            'key_features': 'Feature 1\nFeature 2',
            'technical_stack': 'Django, React',
            'deliverables': 'Code, Docs',
            'timeline': '1 month',
            'additional_info': 'None'
        }
        description = description_for_project(form_data)
        self.assertIn("**Project Title:** Test Title", description)
        self.assertIn("**Key Features:**", description)

    def test_get_request(self):
        request = self.factory.get(reverse('gpt'))
        request.user = self.user

        response = gpt(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form")
    
    def test_valid_form_submission(self):
        data = {
            'title': 'Test Project',
            'goal': 'Create a test project.',
            'target_users': 'Developers',
            'problem_motivation': 'Test problem.',
            'technical_stack': 'Django, React',
            'key_features': 'Feature 1\nFeature 2',
            'deliverables': 'Complete app',
            'timeline': '1 month',
            'additional_info': 'No additional info'
        }

        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('gpt'), data)

        self.assertEqual(response.status_code, 200)
    
    def test_error_handling(self):
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)