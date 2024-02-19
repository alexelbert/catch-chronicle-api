from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    bio = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    catches_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    class Meta:
        model = Profile
        fields = [
            'id', 
            'owner',
            'is_owner', 
            'created_at', 
            'updated_at', 
            'catches_count',
            'name',
            'bio', 
            'location', 
            'profile_picture', 
            'facebook_url', 
            'twitter_url', 
            'instagram_url',
        ]