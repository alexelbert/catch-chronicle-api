from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer that enables the retrieval of the current user's profile ID and profile_image 
    on the API endpoint designated for the current user. 
    Instructions from the CI DRF Walkthrough project.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 
            'profile_image'
        )