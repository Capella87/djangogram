from django.db import models
from django.conf import settings
from django.utils.timezone import now
from user.models import Profile

# Create your models here.
# Djangogram model


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(null=None)
    longitude = models.FloatField(null=None)

    class Meta:
        db_table = 'Location'


class Posts(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    location = models.ForeignKey(Location, on_delete=models.RESTRICT, default=None, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    is_private = models.BooleanField(default=False)
    text = models.TextField()
    is_allow_comment = models.BooleanField(default=True)

    class Meta:
        db_table = 'Posts'


class Mentions(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    mentioner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    mentionee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')

    class Meta:
        db_table = 'Mentions'


class Pictures(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    path = models.CharField(max_length=256)

    class Meta:
        db_table = 'Pictures'


class Videos(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    path = models.CharField(max_length=256)

    class Meta:
        db_table = 'Videos'


class Hashtags(models.Model):
    name = models.CharField(max_length=256)


class Hashtags_usage(models.Model):
    hashtag = models.ForeignKey(Hashtags, on_delete=models.RESTRICT, related_name='+')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')


class Comments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    text = models.TextField(null=False)
    created_date = models.DateTimeField(default=now, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    mention = models.ForeignKey(Mentions, on_delete=models.SET_NULL, related_name='+', null=True)


class Collections(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')

