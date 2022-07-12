from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', MedicalList.as_view(), name="medical-list"),
    url(r'^add/$', MedicalCreate.as_view(), name="medical-create"),
    url(r'^email/(?P<user_id>\d+)/$', MedicalList.as_view(), name='ad-email'),
    url(r'^(?P<pk>\d+)/$', MedicalDetails.as_view(), name="medical-details"),
    url(r'^(?P<pk>\d+)/edit/$', MedicalUpdate.as_view(), name="medical-update"),
    url(r'^(?P<pk>\d+)/delete/$', MedicalDelete.as_view(), name="medical-delete"),
    url(r'^search/$', MedicalSearch.as_view(), name="medical-search"),
]
