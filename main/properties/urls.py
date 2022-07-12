from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^rent/$', PropertiesRentList.as_view(), name="properties_rent-list"),
    url(r'^rent/add/$', PropertiesRentCreate.as_view(), name="properties_rent-create"),
    url(r'^rent/email/(?P<user_id>\d+)/$', PropertiesRentList.as_view(), name='ad-email'),
    url(r'^rent/(?P<pk>\d+)/$', PropertiesRentDetails.as_view(), name="properties_rent-details"),
    url(r'^rent/(?P<pk>\d+)/edit/$', PropertiesRentUpdate.as_view(), name="properties_rent-update"),
    url(r'^rent/(?P<pk>\d+)/delete/$', PropertiesRentDelete.as_view(), name="properties_rent-delete"),
    url(r'^rent/search/$', PropertiesRentSearch.as_view(), name="properties-search"),
    url(r'^sales/$', PropertiesSalesList.as_view(), name="properties_sales-list"),
    url(r'^sales/add/$', PropertiesSalesCreate.as_view(), name="properties_sales-create"),
    url(r'^sales/email/(?P<user_id>\d+)/$', PropertiesSalesList.as_view(), name='ad-email'),
    url(r'^sales/(?P<pk>\d+)/$', PropertiesSalesDetails.as_view(), name="properties_sales-details"),
    url(r'^sales/(?P<pk>\d+)/edit/$', PropertiesSalesUpdate.as_view(), name="properties_sales-update"),
    url(r'^sales/(?P<pk>\d+)/delete/$', PropertiesSalesDelete.as_view(), name="properties_sales-delete"),
    url(r'^sales/search/$', PropertiesSalesSearch.as_view(), name="properties-search"),
]
