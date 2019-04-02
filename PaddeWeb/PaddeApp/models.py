from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    favorite_turtle_name = models.CharField(max_length=50)
    profileinfo = models.TextField(default='svendbent')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class FavoriteTurtle(models.Model):
    title = models.CharField(max_length=200)
    turtleinfo = models.TextField()

    def __unicode__(self):
        return self.title
