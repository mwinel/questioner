"""
Specify URLs as endpoints to consume our API.
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuestionView


urlpatterns = {
    url(r'^questions/$', QuestionView.as_view(), name="create")
}

# Specify the data format.
urlpatterns = format_suffix_patterns(urlpatterns)
