# api/urls.py

from django.urls import path
from .views import SentimentAnalysisView

urlpatterns = [
    path('predict/', SentimentAnalysisView.as_view(), name='sentiment-predict'),
]
