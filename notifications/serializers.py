from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for Notification model.
    """
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Notification
        fields = ('id', 'user', 'created_at', 'notification_type', 'notification_text', 'is_read')
        read_only_fields = ('id', 'user', 'created_at', 'notification_type', 'notification_text', 'is_read')
