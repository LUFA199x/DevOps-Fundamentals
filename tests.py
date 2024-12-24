from django.test import TestCase
from .models import User

#class HomeIntegrationTest(TestCase): = 


class UserUnitTest(TestCase): 

    def setUp(self):
        self.user = User(full_name="john smith")

    def test_uniform_name(self):
        self.assertEqual(self.user.uniform_name(), "John Smith")
 
    def test_capitalized_name(self):
        self.assertEqual(self.user.capitalize(), "JOHN SMITH")

    def test_slug_name(self):
        self.assertEqual(self.user.slug(), "john-smith")