from django.test import TestCase
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
