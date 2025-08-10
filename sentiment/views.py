from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import analyze_sentiment

class SentimentAnalysisView(APIView):
    def post(self, request):
        try:
            text = request.body.decode('utf-8').strip()
        except Exception:
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        if not text:
            return Response({"error": "Text is required."}, status=status.HTTP_400_BAD_REQUEST)

        result = analyze_sentiment(text)
        return Response(result, status=status.HTTP_200_OK)
