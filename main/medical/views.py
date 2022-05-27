from datetime import date
from rest_framework import generics
from .serializers import MedicalSerializer
from main.models import Car_Rent
from rest_framework.permissions import AllowAny

model_name = Car_Rent

class MedicalList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [AllowAny]


class MedicalDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [AllowAny]


class MedicalDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer


class MedicalCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class MedicalUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())
