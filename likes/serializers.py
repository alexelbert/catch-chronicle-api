from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for Like model.
    Included method for making sure user can only make one like per catch.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'created_at',
            'owner',
            'catchId'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already liked this catch.'
            })
