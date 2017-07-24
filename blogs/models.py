from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User, UserManager

class Post(models.Model):
    STATUS_PUBLISH = (
        ('publish', 'Publish'),
        ('expectation', 'Expectation'),
        ('no publish', 'No Publish')
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(upload_to="post_images")
    status = models.CharField(
        max_length=20,
        choices=STATUS_PUBLISH,
        default='expectation',
        blank=True,
        null=True
    )
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    author = models.ForeignKey('auth.User')
