"""
The QuestionSerializer class converts data from django complex database querysets 
to JSON format.

The ModelSerializer class automatically creates a Serializer class with
fields that correspond to the question model fields.
"""

from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Map the question model instance into JSON format."""

    class Meta:
        """Map serializer fields to model fields."""

        model = Question
        fields = ('id', 'title', 'body', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
