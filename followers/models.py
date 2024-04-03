from django.db import models
from django.contrib.auth.models import User
from notifications.models import Notification


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
    
    def save(self, *args, **kwargs):
        # Create a notification when a user is followed
        if not self.pk:  # Only on creation
            Notification.objects.create(
                user=self.followed,
                notification_type='Follow',
                notification_text=f'{self.owner.username} started following you.'
            )
        super().save(*args, **kwargs)
