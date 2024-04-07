from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializes Notification instances, displaying usernames and using
    naturaltime for readable timestamps. Fields are read-only to
    prevent modification via API.
    """
    user = serializers.ReadOnlyField(source="user.username")
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id', 'user', 'created_at', 'notification_type',
            'notification_text', 'is_read'
        )
        read_only_fields = fields

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
