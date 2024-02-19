from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    bio = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    catches_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            return following.id if following else None
        return None
    

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
            'following_count',
            'followers_count',
        ]