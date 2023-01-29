from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    author = models.ForeignKey("users.User", related_name="ad", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='logos/', null=True)


class Comment(models.Model):
    text = models.CharField(max_length=500, null=False, blank=False)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False)
    ad = models.ForeignKey("Ad", on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
