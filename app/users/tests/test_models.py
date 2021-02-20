from django.test import TestCase
from users.models import User

testUser = "john"
testUserManager = "Luke"


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            testUser, 'lennon@thebeatles.com', 'johnpassword')

    def test_user(self):
        jason = User.objects.get(name=testUser)
        self.assertEqual(jason.name, "moo")
        self.assertEqual(jason.speak(), f'{testUser} says hello')


# class ManagerTestCase(TestCase):
