from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anomymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=100, db_index=True
     )

    likecount = models.IntegerField(
        'like_count', default=0, blank=True
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True
    )
    created_at = models.DateTimeField(
        'created DateTime', blank=True, auto_now_add=True
    )
