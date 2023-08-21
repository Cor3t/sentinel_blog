from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField()
    on_created = models.DateTimeField(auto_now_add=True)
    on_updated = models.DateTimeField(auto_now=True)


