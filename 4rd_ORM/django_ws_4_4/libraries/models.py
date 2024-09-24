from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.TextField()
    salespoint = models.IntegerField()
    adult = models.BooleanField()
    link = models.URLField()
    pubdate = models.DateField()