from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^submit$', submit),
    url(r'^results$', results),
    url(r'^home$', index),
]