from django.test import TestCase
from users.models import User

testUserEmail = "lennon@thebeatles.com"
password = 'mypassword'


class UserTests(TestCase):
    def setUp(self):

        User.objects.create_user(
            email=testUserEmail, password=password)

    def test_user(self):
        user = User.objects.get(email=testUserEmail)
        self.assertEqual(user.email, testUserEmail)
