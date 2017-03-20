from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='secrets_index'),
    url(r'^register$', register, name='secrets_register'),
    url(r'^login$', login, name='secrets_login'),
    url(r'^recent$', recent, name='secrets_recent'),
    url(r'^submit$', submit, name='secret_submit'),
    url(r'^popular$', popular, name='secrets_popular'),
    url(r'^like/(?P<id>\d+)$', like, name='like_secret'),
    url(r'^unlike/(?P<id>\d+)$', unlike, name='unlike_secret'),
]