from django.db import models

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(default=0)  # Add this field to track hits

    def __str__(self):
        return self.short_url
