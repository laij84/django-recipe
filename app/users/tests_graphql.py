import graphene
from django.test import TestCase
from snapshottest import TestCase as SnapshotTestCase, snapshot
from graphene.test import Client

import graphene
from django.utils.functional import SimpleLazyObject

from .models import User

from app.schema import schema, Query

class UserTests(TestCase):
    email = "111@test.com"
    password = "password"
    def setUp(self):
        
        self.user = User.objects.create_user(email=self.email, password=self.password)
        self.schema = graphene.Schema(query=Query)

    def test_single_user(self):
        query = '''
        query {
            users {
                id
                email
                password
            }
        }
        '''
        expected = [{
            "id": str(self.user.id),
            'email': self.email,
            "password": self.user.password
        
        }]
        response = self.schema.execute(query)
        self.assertDictEqual(response.data, { 'users': expected })


class SnapshotTests(SnapshotTestCase):
    email = "111@test.com"
    password = "password"
    def setUp(self):
        self.client = Client(schema)
        self.user = User.objects.create_user(email=self.email, password=self.password)

    def test_snapshot_users(self):
        query = """
            query users {
                users {
                    email
                }
            }
        """
        self.assertMatchSnapshot(self.client.execute(query))

