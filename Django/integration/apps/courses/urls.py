from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='course_index'),
    url(r'^coursesubmission$', coursesubmission, name='submit'),
    url(r'^delete/(?P<id>\d+)$', deletecourse, name='course_delete'),
    url(r'^confirmdelete/(?P<id>\d+)$', confirmdelete, name='confirm_delete'),
    url(r'^canceldelete$', index, name='cancel_delete'),
    url(r'^assignment$', assignment, name='assignment'),
    url(r'^assign_submit$', assign_submit, name='assign_submit'),
]