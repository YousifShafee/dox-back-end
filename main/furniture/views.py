from datetime import date
from rest_framework import generics
from .serializers import FurnitureSerializer
from main.models import Furniture_ad
from rest_framework.permissions import AllowAny

model_name = Furniture_ad

class FurnitureList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]


class FurnitureDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]


class FurnitureDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer


class FurnitureCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class FurnitureUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())
