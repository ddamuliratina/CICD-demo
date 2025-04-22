from django.test import TestCase, Client
from django.urls import reverse

class GreetingTests(TestCase):
    def setUp(self):
        self.client = Client()
        

    def test_greeting_view(self):
        response = self.client.get(reverse("index"))  # Adjust the URL name if necessary
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello!")  # Adjust this based on your actual greeting message
        self.assertTemplateUsed(response, "index.html")
        
class GreetingFunctionalityTests(TestCase):
    def test_greeting(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["greeting"], "Hello!")  # Adjust this based on your actual greeting message
