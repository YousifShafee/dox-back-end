from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', FurnitureList.as_view(), name="furniture-list"),
    url(r'^add/$', FurnitureCreate.as_view(), name="furniture-create"),
    url(r'^(?P<pk>\d+)/$', FurnitureDetails.as_view(), name="furniture-details"),
    url(r'^(?P<pk>\d+)/edit/$', FurnitureUpdate.as_view(), name="furniture-update"),
    url(r'^(?P<pk>\d+)/delete/$', FurnitureDelete.as_view(), name="furniture-delete"),
    url(r'^search/$', FurnitureSearch.as_view(), name="furniture-search"),
]
