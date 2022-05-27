from datetime import date
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import CarRentSerializer, CarSalesSerializer
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
