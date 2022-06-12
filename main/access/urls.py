from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', AccessList.as_view(), name="access-list"),
    url(r'^add/$', AccessCreate.as_view(), name="access-create"),
    url(r'^(?P<pk>\d+)/$', AccessDetails.as_view(), name="access-details"),
    url(r'^(?P<pk>\d+)/edit/$', AccessUpdate.as_view(), name="access-update"),
    url(r'^(?P<pk>\d+)/delete/$', AccessDelete.as_view(), name="access-delete"),
    url(r'^search/$', AccessSearch.as_view(), name="access-search"),
]
