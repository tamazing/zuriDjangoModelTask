from datetime import datetime
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
#User = settings.AUTH_USER_MODEL

User = get_user_model()

# Create your models here.


class Post(models.Model):
    Title: models.CharField(max_length=200)
    Text: models.TextField()
    Author: models.ForeignKey(User, on_delete=models.SET_DEFAULT)
    Created_date: models.DateTimeField('Date created:', default=datetime.now())
    Published_date: models.DateTimeField(
        'Date published:', default=datetime.now())

#
# Author : A Foreign Key to the current user model.
#         Make use of Django’s get_user_model function.
