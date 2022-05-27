from django.conf.urls import url
from django.urls import path
from .views import ImageList

urlpatterns = [
    path('', ImageList.as_view(), name='image'),
    url(r'^(?P<category>[\w-]+)/$', ImageList.as_view(), name='image'),
]
