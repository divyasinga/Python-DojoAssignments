from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^coursesubmission$', coursesubmission),
    url(r'^delete/(?P<id>\d+)$', deletecourse),
    url(r'^confirmdelete/(?P<id>\d+)$', confirmdelete),
    url(r'^canceldelete$', index),
]