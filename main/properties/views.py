from datetime import date
from rest_framework import generics
from .serializers import PropertiesRentSerializer, PropertiesSalesSerializer
from main.models import Properties_Rent, Properties_Sales
from rest_framework.permissions import AllowAny


class PropertiesSalesList(generics.ListAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer
    permission_classes = [AllowAny]


class PropertiesSalesDetails(generics.RetrieveAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer
    permission_classes = [AllowAny]


class PropertiesSalesDelete(generics.DestroyAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer


class PropertiesSalesCreate(generics.CreateAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class PropertiesSalesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())

class PropertiesRentList(generics.ListAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer
    permission_classes = [AllowAny]


class PropertiesRentDetails(generics.RetrieveAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer
    permission_classes = [AllowAny]


class PropertiesRentDelete(generics.DestroyAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer


class PropertiesRentCreate(generics.CreateAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class PropertiesRentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())
