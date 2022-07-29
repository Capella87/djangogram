from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    username = models.CharField(max_length=100, null=False, default=None)
    birthday = models.DateField()
    website = models.TextField(null=True)
    shown_name = models.CharField(max_length=100, null=True)
    gender = models.IntegerField()
    bio = models.TextField(null=True)
    is_private = models.BooleanField(default=False)
    picture = models.ImageField(default=None, null=True, upload_to='profile_images')