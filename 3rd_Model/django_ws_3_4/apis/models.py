from django.db import models

# Create your models here.
class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.TextField()
    documentation_url = models.TextField()
    auth_required = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    sample_data = models.JSONField()