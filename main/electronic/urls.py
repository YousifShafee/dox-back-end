from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ElectronicList.as_view(), name="electronic-list"),
    url(r'^add/$', ElectronicCreate.as_view(), name="electronic-create"),
    url(r'^(?P<pk>\d+)/$', ElectronicDetails.as_view(), name="electronic-details"),
    url(r'^(?P<pk>\d+)/edit/$', ElectronicUpdate.as_view(), name="electronic-update"),
    url(r'^(?P<pk>\d+)/delete/$', ElectronicDelete.as_view(), name="electronic-delete"),
    url(r'^search/$', ElectronicSearch.as_view(), name="electronic-search"),
]
