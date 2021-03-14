from django.test import TestCase
from accounts.models import UserData

# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        UserData.objects.create(userId=1001, title="hello satya", body="How are you?")


    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_upload_page_status_code(self):
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_status_code(self):
        response = self.client.get('/detail/')
        self.assertEqual(response.status_code, 200)

    def test_user_content(self):
        user=UserData.objects.get(userId=1001)
        expected_user_output = f'{user.body}'
        self.assertEqual(expected_user_output, 'How are you?')
