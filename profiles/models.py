from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class for the profile model OneToOne relationship
    with the User model Profile that is automatically created
    by Django signal when user is created
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(
        upload_to='images/', default='../default_profile_zsweuz'
    )
    facebook_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    instagram_url = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Return info of the profile owner
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
