from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from index.models import Message
from .forms import SendMessageForm

class MessageViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='Test1234')
        self.client.login(username='test_user', password='Test1234')

    def test_send_message_view(self):
        response = self.client.get(reverse('send_message'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sendmessage.html')

        # Test sending a message
        form_data = {
            'to_user': 0,
            'title': 'Test Message',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('send_message'), form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful submission
        self.assertEqual(Message.objects.count(), 1)  # Message should be saved in the database
        # Check if to_user_id is properly set
        self.assertEqual(Message.objects.first().to_user_id, 0)

if __name__ == '__main__':
    unittest.main()
