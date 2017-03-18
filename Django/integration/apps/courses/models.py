from __future__ import unicode_literals
from ..loggy.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Enrollment(models.Model):
    course_enrolled = models.ForeignKey(Course, related_name='course_enrolled', blank=True, null=True)
    user_student = models.ForeignKey(User, related_name='user_enrolled', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)