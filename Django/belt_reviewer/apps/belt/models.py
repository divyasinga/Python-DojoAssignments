from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.{8,32}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*')
NAME_REGEX =  re.compile(r'^[a-zA-Z]+$')

# Create your models here.
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
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    objects = EmailManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating_options = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating = models.IntegerField(choices=rating_options)
    reviewer = models.ForeignKey(User)
    book = models.ForeignKey(Book, related_name="bookreview")
    review_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bookauthored = models.ForeignKey(Book, blank=True, null=True, related_name="bookauthored")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)