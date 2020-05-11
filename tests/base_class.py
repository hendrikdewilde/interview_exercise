from django.contrib.auth.models import User
from django.test import TestCase


class BaseTestCase(TestCase):
    """
    Will use django.test
    With sqlite3 - remember it only do migrations for initial and not other
    migrations after initial. It is a bug
    """
    def setUp(self):
        # Setup run before every test method.
        User.objects.create(username="user1", email="user1@mail.co.za")
        User.objects.create(username="user2", email="user2@mail.co.za")
        User.objects.create(username="user3", email="user3@mail.co.za")

    def tearDown(self):
        # Clean up run after every test method.
        pass



