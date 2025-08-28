from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=25)
    logo = models.ImageField(upload_to="company", blank=True, null=True)
    call_us = models.CharField(max_length=25, blank=True, null=True)
    email_us = models.EmailField(blank=True, null=True)
    subtitle = models.TextField(max_length=500)
    fb_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    emails = models.TextField(max_length=100, blank=True, null=True)
    numbers = models.TextField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.name
