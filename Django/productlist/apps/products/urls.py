from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index, name='product_index'),
    url(r'^new$', new, name='new_product'),
    url(r'^submit_new$', submit_new, name='submit_new'),
    url(r'^edit/(?P<id>\d+)$', edit, name='edit_product'),
    url(r'^submit_edit$', submit_edit, name='submit_edit'),
    url(r'^show/(?P<id>\d+)$', show, name='show_product'),
    url(r'^delete/(?P<id>\d+)$', delete, name='delete_product'),
    url(r'^submit_delete$', submit_delete, name='submit_delete'),
]
