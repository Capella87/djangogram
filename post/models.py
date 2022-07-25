from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(null=None)
    longitude = models.FloatField(null=None)

class Post(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location.id, on_delete=models.RESTRICT, default=None)
    created_date = models.DateTimeField(default=now, editable=False)
    text = models.TextField()

class Mentions(models.Model):
    post_id = models.ForeignKey(Post.id, on_delete=models.CASCADE)
    mentioner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mentionee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Pictures(models.Model):
    post_id = models.ForeignKey(Post.id, on_delete=models.CASCADE)