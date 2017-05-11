from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "User: " + self.user

class Activities (models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    detail = models.TextField(max_length = 1000, blank = False)
    point = models.IntegerField(default=0, blank= False)
    InProgress = models.BooleanField(default=False)

    def __str__(self):
        return 'Activity {} do {} and gain {}{}'.format(self.name, self.detail, self.point, self.InProgress)

class MyActivities (models.Model):
    add_date = models.DateTimeField(blank=False)
    user = models.ForeignKey('auth.User', blank=False)
    activities = models.ForeignKey(Activities)

    def __str__(self):
        return 'User {} with detail {} at {}'.format(self.user, self.activities, self.add_date)


class ChatRoom(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message
