from django.db import models
from django.contrib.auth.models import User
from catches.models import Catch


class Like(models.Model):
    """
    Like model, related to owner and Catch.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    catch = models.ForeignKey(
        Catch,
        related_name='likes',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'catch']

    def __str__(self):
        return f'{owner} {self.catch}'
