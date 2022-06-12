from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^rent/$', CarRentList.as_view(), name="car_rent-list"),
    url(r'^rent/add/$', CarRentCreate.as_view(), name="car_rent-create"),
    url(r'^rent/(?P<pk>\d+)/$', CarRentDetails.as_view(), name="car_rent-details"),
    url(r'^rent/(?P<pk>\d+)/edit/$', CarRentUpdate.as_view(), name="car_rent-update"),
    url(r'^rent/(?P<pk>\d+)/delete/$', CarRentDelete.as_view(), name="car_rent-delete"),
    url(r'^rent/search/$', CarRentSearch.as_view(), name="car-search"),
    url(r'^sales/$', CarSalesList.as_view(), name="car_sales-list"),
    url(r'^sales/add/$', CarSalesCreate.as_view(), name="car_sales-create"),
    url(r'^sales/(?P<pk>\d+)/$', CarSalesDetails.as_view(), name="car_sales-details"),
    url(r'^sales/(?P<pk>\d+)/edit/$', CarSalesUpdate.as_view(), name="car_sales-update"),
    url(r'^sales/(?P<pk>\d+)/delete/$', CarSalesDelete.as_view(), name="car_sales-delete"),
    url(r'^sales/search/$', CarSalesSearch.as_view(), name="car-search"),
]
