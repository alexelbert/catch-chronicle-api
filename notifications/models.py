from django.db import models
from django.contrib.auth.models import User
from catches.models import Catch

class Notification(models.Model):
    """
    Notification model to store notifications for users.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=20)  # Like, Follow, Comment
    notification_text = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.notification_text
