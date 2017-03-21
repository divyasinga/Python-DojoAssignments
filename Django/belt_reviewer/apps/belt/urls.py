from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='reviewer_index'),
    url(r'^register$', register, name='reviewer_register'),
    url(r'^login$', login, name='reviewer_login'),
    url(r'^recent$', recent, name='reviewer_recent'),
    url(r'^reviewpost$', post, name='reviewer_post'),
    url(r'^submit$', submit, name='reviewer_submit'),
    url(r'^logout$', logout, name='logout'),
    url(r'^book/(?P<id>\d+)$', book, name='bookinfo'),
    url(r'^user/(?P<id>\d+)$', user, name='userinfo'),
]
