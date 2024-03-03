from django.db import models
from django.contrib.auth.models import User


class Catch(models.Model):
    """
    Model to represent a catch made by a user.
    Containing geolocation data and predefined lists.
    """

    METHOD_CHOICES = [
        ('flyrod', 'Fly Rod'),
        ('spinning', 'Spinning'),
        ('trolling', 'Trolling'),
    ]

    WEATHER_CHOICES = [
        ('sunny', 'Sunny'),
        ('cloudy', 'Cloudy'),
        ('rainy', 'Rainy'),
        ('stormy', 'Stormy'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_zsweuz',
        blank=False
    )

    species = models.CharField(max_length=100)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    time = models.TimeField()
    weather = models.CharField(max_length=20, choices=WEATHER_CHOICES)
    lure = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username}\'s catch: {self.caption}'
