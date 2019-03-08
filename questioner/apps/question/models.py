from django.db import models


class Question(models.Model):
    """This class represents the question model."""

    title = models.CharField(max_length=200, blank=False, unique=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a readable representation of the model instance."""
        return "{}".format(self.title)
