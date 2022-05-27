from datetime import date
from rest_framework import generics
from .serializers import MedicalSerializer
from main.models import Car_Rent
from rest_framework.permissions import AllowAny

model_name = Car_Rent

class AccessList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer


class AccessDetails(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer


class AccessDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer


class AccessCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class AccessUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())
