from django.db import models

class Feedback(models.Model):
    text = models.TextField()  # user-written feedback
    sentiment = models.CharField(max_length=20, default='Unprocessed')  # auto-tagged later
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp added automatically

    def __str__(self):
        return self.text[:50]  # shows first 50 chars in admin panel

