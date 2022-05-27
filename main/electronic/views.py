from datetime import date
from rest_framework import generics
from .serializers import ElectronicSerializer
from main.models import Electronic_ad
from rest_framework.permissions import AllowAny

model_name = Electronic_ad

class ElectronicList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [AllowAny]


class ElectronicDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [AllowAny]


class ElectronicDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer


class ElectronicCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class ElectronicUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())
