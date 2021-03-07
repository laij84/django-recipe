import json
from django.urls import reverse
from django.test import TestCase, Client as TestClient
from users.models import User
from django.contrib import admin

from graphene_django.utils.testing import GraphQLTestCase

from graphene.test import Client
from app.schema import schema

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

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = TestClient()
        self.admin_user = User.objects.create_superuser(email="admin@meow.com", password="password")
        
        self.client.force_login(self.admin_user)

        self.user = User.objects.create_user(email="user@meow.com", password="password")

    def test_users_are_listed(self):
        url = reverse('admin:users_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)