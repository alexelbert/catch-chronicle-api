from rest_framework import serializers
from .models import Catch


class CatchSerializer(serializers.ModelSerializer):
    """
    Serializer for Catch model
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                "Image can't be larger then 2MB!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width can't be larger then 4096px"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height can't be larger then 4096px"
            )
        return value
    
    def get_is_owner(self, obj):
        return obj.owner == self.context["request"].user


    class Meta:
        model = Catch
        fields = [
            'id', 
            'owner', 
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at', 
            'title', 
            'species', 
            'method', 
            'weight', 
            'length', 
            'location', 
            'time', 
            'weather', 
            'lure'
        ]
