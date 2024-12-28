from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    issue = models.TextField()
    photo = models.ImageField(upload_to='feedback_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'} - {self.created_at}"
