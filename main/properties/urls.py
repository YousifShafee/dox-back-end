from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', PropertiesRentList.as_view(), name="properties_rent-list"),
    url(r'^add/$', PropertiesRentCreate.as_view(), name="properties_rent-create"),
    url(r'^(?P<pk>\d+)/$', PropertiesRentDetails.as_view(), name="properties_rent-details"),
    url(r'^(?P<pk>\d+)/edit/$', PropertiesRentUpdate.as_view(), name="properties_rent-update"),
    url(r'^(?P<pk>\d+)/delete/$', PropertiesRentDelete.as_view(), name="properties_rent-delete"),
    url(r'^$', PropertiesSalesList.as_view(), name="properties_sales-list"),
    url(r'^add/$', PropertiesSalesCreate.as_view(), name="properties_sales-create"),
    url(r'^(?P<pk>\d+)/$', PropertiesSalesDetails.as_view(), name="properties_sales-details"),
    url(r'^(?P<pk>\d+)/edit/$', PropertiesSalesUpdate.as_view(), name="properties_sales-update"),
    url(r'^(?P<pk>\d+)/delete/$', PropertiesSalesDelete.as_view(), name="properties_sales-delete"),
]
