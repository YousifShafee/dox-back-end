from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', MobileList.as_view(), name="mobile-list"),
    url(r'^add/$', MobileCreate.as_view(), name="mobile-create"),
    url(r'^email/(?P<user_id>\d+)/$', MobileList.as_view(), name='ad-email'),
    url(r'^(?P<pk>\d+)/$', MobileDetails.as_view(), name="mobile-details"),
    url(r'^(?P<pk>\d+)/edit/$', MobileUpdate.as_view(), name="mobile-update"),
    url(r'^(?P<pk>\d+)/delete/$', MobileDelete.as_view(), name="mobile-delete"),
    url(r'^search/$', MobileSearch.as_view(), name="mobile-search"),
]
