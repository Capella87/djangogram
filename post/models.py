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
    is_private = models.BooleanField(default=False)
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
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    path = models.CharField(max_length=256)

    class Meta:
        db_table = 'Pictures'

class Videos(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    created_date = models.DateTimeField(default=now, editable=False)
    path = models.CharField(max_length=256)

    class Meta:
        db_table = 'Videos'

class Hashtags(models.Model):
    name = models.CharField(max_length=256)

class Hashtags_usage(models.Model):
    hashtag_id = models.ForeignKey(Hashtags, on_delete=models.RESTRICT, related_name='+')
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='+')
class Comments(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post.id, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(default=now, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    mention_id = models.ForeignKey(Mentions.id, on_delete=models.CASCADE)
