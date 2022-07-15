from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^$', ImageList.as_view(), name='image-list'),
    url(r'^add/$', ImageCreateAPIView.as_view(), name="image-create"),
    url(r'^search/$', ImageSearch.as_view(), name="image-search"),
    url(r'^(?P<pk>\d+)/edit/$', ImageUpdate.as_view(), name="ad-update"),
    url(r'^(?P<pk>\d+)/delete/$', ImageDelete.as_view(), name="image-delete"),
    url(r'^(?P<pk>\d+)/active/$', ActiveImageUpdate.as_view(), name="active-ad"),
    url(r'^(?P<category>[\w-]+)/(?P<active>[\w-]+)/$', ImageList.as_view(), name='image-category'),
]
