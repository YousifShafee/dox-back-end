from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', ImageList.as_view(), name='image'),
    url(r'^add/$', ImageCreateAPIView.as_view(), name="image-create"),
    url(r'^(?P<category>[\w-]+)/$', ImageList.as_view(), name='image'),
    url(r'^(?P<pk>\d+)/edit/$', ImageUpdate.as_view(), name="ad-update"),
    url(r'^(?P<pk>\d+)/delete/$', ImageDelete.as_view(), name="image-delete"),
]
