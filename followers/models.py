from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model for the relationship between users, indicating who is following whom.
    """

    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
