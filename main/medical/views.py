from datetime import date
from rest_framework import generics, views, response
from .serializers import MedicalSerializer
from main.models import Medical_ad
from main.general_fun import get_data_by_field
from rest_framework.permissions import AllowAny

model_name = Medical_ad

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


class MedicalSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = MedicalSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'price': 'ad_id__price__range',
    'type': 'type',
    'condition': 'condition',
}