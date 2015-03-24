import unittest
from django.test import TestCase, Client

# Create your tests here.

class LoginTest(unittest.TestCase):
    def testLogin(self):
        # Test to see that the login view is working
        c = Client()
        response = c.post('/login/', 
            {'email': 'TestStudent', 'password': 'TestStudent'})
        response.status_code
        self.assertEqual(response.status_code, 200)

