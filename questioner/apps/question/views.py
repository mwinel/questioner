from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


class QuestionView(generics.ListCreateAPIView):
    """This class handles the HTTP GET(all) and POST methods."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def question(self, serializer):
        """Save question data on post."""
        serializer.save()
