from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^ninja$', ninjas),
    url(r'^ninja/(?P<id>\D+)$', turtles),
]