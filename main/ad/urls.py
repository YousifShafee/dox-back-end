from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', AdList.as_view(), name="ad-list"),
    url(r'^add/$', AdCreate.as_view(), name="ad-create"),
    url(r'^email/(?P<user_id>\d+)/$', AdList.as_view(), name='ad-email'),
    url(r'^(?P<pk>\d+)/$', AdDetails.as_view(), name="ad-details"),
    url(r'^(?P<pk>\d+)/edit/$', AdUpdate.as_view(), name="ad-update"),
    url(r'^(?P<pk>\d+)/delete/$', AdDelete.as_view(), name="ad-delete"),
    url(r'^search/$', AdSearch.as_view(), name="ad-search"),
]
