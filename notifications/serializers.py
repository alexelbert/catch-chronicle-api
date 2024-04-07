from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for Notification model.
    """
    user = serializers.ReadOnlyField(source="user.username")
    created_at = serializers.SerializerMethodField()  # Modify the created_at field

    class Meta:
        model = Notification
        fields = ('id', 'user', 'created_at', 'notification_type', 'notification_text', 'is_read')
        read_only_fields = ('id', 'user', 'created_at', 'notification_type', 'notification_text', 'is_read')

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
