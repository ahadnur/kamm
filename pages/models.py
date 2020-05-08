from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.description[:200]