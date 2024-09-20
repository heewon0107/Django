from django.db import models
from django.core.validators import URLValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=60)
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
