from datetime import date
from rest_framework import generics
from .serializers import MobileSerializer
from main.models import Mobile_ad
from rest_framework.permissions import AllowAny

model_name = Mobile_ad

class MobileList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer
    permission_classes = [AllowAny]


class MobileDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer
    permission_classes = [AllowAny]


class MobileDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer


class MobileCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class MobileUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())
