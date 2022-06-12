from main.general_fun import get_data_by_field
from datetime import date
from rest_framework.permissions import AllowAny
from rest_framework import generics, views, response
from .serializers import CarSalesSerializer, CarRentSerializer
from main.models import Car_Rent, Car_Sales


class CarSalesList(generics.ListAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer
    permission_classes = [AllowAny]


class CarSalesDetails(generics.RetrieveAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer
    permission_classes = [AllowAny]


class CarSalesDelete(generics.DestroyAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer


class CarSalesCreate(generics.CreateAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class CarSalesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class CarSalesSearch(views.APIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = Car_Sales.objects.filter(**q)
        result = CarSalesSerializer(model_data, many=True).data
        return response.Response(result)


class CarRentList(generics.ListAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer
    permission_classes = [AllowAny]


class CarRentDetails(generics.RetrieveAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer
    permission_classes = [AllowAny]


class CarRentDelete(generics.DestroyAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer


class CarRentCreate(generics.CreateAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class CarRentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class CarRentSearch(views.APIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = Car_Rent.objects.filter(**q)
        result = CarRentSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'brand': 'car__brand__brand',
    'model': 'car__brand__model',
    'price': 'ad_id__price__range',
    'condition': 'car__condition',
    'color': 'car__color',
    'year': 'car__year',
    'kilometer': 'kilometer',
    'transmission_type': 'car__transmission_type',
    'fuel_type': 'car__fuel_type',
    'engine_capacity': 'car__engine_capacity',
    'ad_type': 'ad_type',
    'body_type': 'car__body_type',
    'rental_option': 'car__rental_option',
    'rental_period': 'car__rental_period',
}