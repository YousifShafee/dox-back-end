from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', CarRentList.as_view(), name="car_rent-list"),
    url(r'^add/$', CarRentCreate.as_view(), name="car_rent-create"),
    url(r'^(?P<pk>\d+)/$', CarRentDetails.as_view(), name="car_rent-details"),
    url(r'^(?P<pk>\d+)/edit/$', CarRentUpdate.as_view(), name="car_rent-update"),
    url(r'^(?P<pk>\d+)/delete/$', CarRentDelete.as_view(), name="car_rent-delete"),
    url(r'^$', CarSalesList.as_view(), name="car_sales-list"),
    url(r'^add/$', CarSalesCreate.as_view(), name="car_sales-create"),
    url(r'^(?P<pk>\d+)/$', CarSalesDetails.as_view(), name="car_sales-details"),
    url(r'^(?P<pk>\d+)/edit/$', CarSalesUpdate.as_view(), name="car_sales-update"),
    url(r'^(?P<pk>\d+)/delete/$', CarSalesDelete.as_view(), name="car_sales-delete"),
]
