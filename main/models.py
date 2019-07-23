from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from chat.models import *

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    obj = models.CharField(max_length=100, blank=True)
    points = ArrayField(models.CharField(
        max_length=200), null=True, blank=True)
    members = models.ManyToManyField(User, related_name='meetings', blank=True)
    chairperson = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    begin = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True)
    previous_meeting = models.OneToOneField(
        'self', on_delete=models.SET_NULL, blank=True, related_name='next', null=True)
    next_meeting = models.OneToOneField(
        'self', on_delete=models.SET_NULL, blank=True, related_name='previous', null=True)
    chatroom = models.OneToOneField(
        ChatRoom, on_delete=models.CASCADE, related_name='meeting', blank=True, null=True)
    done = models.BooleanField(default=False)
    doing = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Gender(models.Model):
    title = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(default='static/images/anonym.png')
    job = models.CharField(max_length=100)
    phone = models.IntegerField()
    description = models.TextField(blank=True)
    contacts = models.ManyToManyField(
        'self', related_name='contacts', blank=True)

    def __str__(self):
        return self.user.username + "_profile"
