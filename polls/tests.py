from django.test import TestCase  # noqa: F401
from django.urls import reverse

# Create your tests here.

class PollTests(TestCase):
    def test_polls_page(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)

    def test_dummy(self):
        self.assertTrue(True)
