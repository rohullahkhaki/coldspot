from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mimetypes import guess_type

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    media = models.FileField(null=True, blank=True, upload_to='post_vid')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def media_type_html(self):
        """
        guess_type returns a tuple like (type, encoding) and we want to access
        the type of media file in first index of tuple
        """
        type_tuple = guess_type(self.media.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"

    def __str__(self):
        return self.title


    def media_type_html(self):
        """
        guess_type returns a tuple like (type, encoding) and we want to access
        the type of media file in first index of tuple
        """
        type_tuple = guess_type(self.media.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"
