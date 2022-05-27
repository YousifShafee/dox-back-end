from django.conf.urls import url
from .views import Logout, UserCreateAPIView, UserDelete, UserDetails, UserList, UserLoginAPIView, UserUpdate

urlpatterns = [
    url(r'^$', UserList.as_view(), name="user-list"),
    url(r'^(?P<pk>\d+)/$', UserDetails.as_view(), name="user-details"),
    url(r'^(?P<pk>\d+)/edit/$', UserUpdate.as_view(), name="user-update"),
    url(r'^(?P<pk>\d+)/delete/$', UserDelete.as_view(), name="user-delete"),
    url(r'^add/$', UserCreateAPIView.as_view(), name="user-create"),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
]
