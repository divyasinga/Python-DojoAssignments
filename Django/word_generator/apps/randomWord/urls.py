from django.conf.urls import url, include
from views import *

urlpatterns = [
    url('^$', index),
    url('^generate$', generate)
]