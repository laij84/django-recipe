from django.test import TestCase
from users.models import User

testUserEmail = "lennon@thebeatles.com"
password = 'mypassword'

class UserTests(TestCase):

    def setUp(self):
        User.objects.create_user(email=testUserEmail, password=password)

    def test_user(self):
        user = User.objects.get(email=testUserEmail)
        self.assertEqual(user.email, testUserEmail)

    def test_normalize_email(self):
        email = 'dog@BARK.com'
        password = 'password'

        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email.lower())

    def test_validate_email(self):
        """Ensure that a proper email address is passed"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'password')

    def test_create_new_superuser(self):
        """Test for creating a superuser"""
        superuser = User.objects.create_superuser(
            email="admin@aol.com", password="password")

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
