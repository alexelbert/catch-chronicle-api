from django.db import models
from django.contrib.auth.models import User

class Catch(models.Model):
    """
    Model to represent a catch made by a user.
    """
    PRIVACY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    
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

    FILTER_CHOICES = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='../default_profile_zsweuz', blank=True)
    image_filter = models.CharField(max_length=32, choices=FILTER_CHOICES, default='normal')

    species = models.CharField(max_length=100)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=255)
    time = models.TimeField()
    weather = models.CharField(max_length=20, choices=WEATHER_CHOICES)
    lure = models.CharField(max_length=50)

    method_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    weight_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    length_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    location_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    time_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    weather_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    lure_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username}\'s catch: {self.title}'
