from __future__ import unicode_literals
import bcrypt
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.{8,32}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*')
NAME_REGEX =  re.compile(r'^[a-zA-Z]+$')

class EmailManager(models.Manager):
    def validate(self, postData):
        if not EMAIL_REGEX.match(postData):
            return False
        else:
            return True
    def validpw(self, postData):
        if not PW_REGEX.match(postData):
            return False
        else:
            return True

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    objects = EmailManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)