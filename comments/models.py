from django.db import models
from django.contrib.auth.models import User
from catches.models import Catch


class Comment(models.Model):
    """
    Comment model, related to User and Catch.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    catchId = models.ForeignKey(Catch, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
