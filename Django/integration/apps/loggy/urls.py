from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='loggy_index'),
    url(r'^validate$', register, name='loggy_validate'),
    url(r'^login$', login, name='loggy_login'),
]
