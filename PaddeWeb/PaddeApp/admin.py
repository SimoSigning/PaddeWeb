from django.contrib import admin
from PaddeApp.models import FavoriteTurtle
from PaddeApp.models import UserProfile
from PaddeApp.models import User
from PaddeApp.models import TurtleForum

# Register your models here.
admin.site.register(FavoriteTurtle)
admin.site.register(UserProfile)
admin.site.register(TurtleForum)