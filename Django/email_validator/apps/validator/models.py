from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, postData):
        if not EMAIL_REGEX.match(postData):
            return False
        else:
            return True

class Email(models.Model):
    email = models.CharField(max_length=50)
    emailManager = EmailManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)