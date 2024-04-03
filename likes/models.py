from django.db import models
from django.contrib.auth.models import User
from catches.models import Catch
from notifications.models import Notification


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
        return f'{self.owner} {self.catch}'

    
    def save(self, *args, **kwargs):
        # Create a notification when a catch is liked
        if not self.pk:  # Only on creation
            Notification.objects.create(
                user=self.catch.owner,
                notification_type='Like',
                notification_text=f'{self.owner.username} liked your catch.'
            )
        super().save(*args, **kwargs)