from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(null=None)
    longitude = models.FloatField(null=None)

    class Meta:
        db_table = 'Location'


class Posts(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    location_id = models.ForeignKey(Location, on_delete=models.RESTRICT, default=None, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    text = models.TextField()

    class Meta:
        db_table = 'Posts'

class Mentions(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    mentioner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    mentionee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')

    class Meta:
        db_table = 'Mentions'

class Pictures(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    user_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    path = models.CharField(max_length=256)

    class Meta:
        db_table = 'Pictures'
