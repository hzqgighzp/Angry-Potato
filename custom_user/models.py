# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name = "Mobile number")
    image = models.ImageField(upload_to="img", default=u"image/default.png", max_length=100)
    wechat = models.CharField(max_length=11, null=True, blank=True, verbose_name="Wechat")
    location = models.CharField(max_length=11, null=True, blank=True, verbose_name="Location")
    class Meta:
        verbose_name = "User information"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username