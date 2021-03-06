# Models.py
"""Models of database."""
from time import process_time_ns
from turtle import pos
from django.db import models
from django.conf import settings


class Db(models.Model):
    """Database class."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=False, 
        on_delete=models.SET_NULL, related_name="+")
    created_at = models.DateTimeField(auto_created=True)
    updated_At = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""

        abstract = True


class Post(Db):
    """Post class."""

    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        """Print Title, User, Content."""
        return 'Title: %s |  User: %s | Content: %s' % (self.title, self.user, self.content)


class Like(Db):
    """Like class."""

    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
