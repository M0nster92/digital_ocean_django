from django.db import models
# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    published = models.DateField(null=True)
