from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Feedback
from .serializers import FeedbackSerializer
from sentiment.utils import analyze_sentiment  # ✅ Import ML logic

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['sentiment', 'created_at']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        feedback = serializer.save()
        result = analyze_sentiment(feedback.text)
        feedback.sentiment = result["sentiment"]
        feedback.save()
