from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Question


class QuestionModelTestCase(TestCase):
    """This class defines the test suite for the Qusetion model."""

    def setUp(self):
        """Define test client and other test variables."""
        self.question_title = "what happened to JFK?"
        self.question = Question(title=self.question_title)

    def test_model_can_create_a_question(self):
        """Test the question model can create a question."""
        old_count = Question.objects.count()
        self.question.save()
        new_count = Question.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_a_representation(self):
        """Test api returns a readble instance of the question model."""
        self.assertEqual(str(self.question), self.question_title)


class QuestionViewTestCase(TestCase):
    """Test suite for the question API views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.question_data = {
                'title': 'who did go to ibiza?', 
                'body': 'In the summer...'
            }
        self.response = self.client.post(
            reverse('create'),
            self.question_data,
            format="json"
        )

    def test_api_can_create_a_question(self):
        """Test api can create a question."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
