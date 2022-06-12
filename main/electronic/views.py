from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response
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


class ElectronicSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = ElectronicSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'price': 'ad_id__price__range',
    'condition': 'condition',
    'brand': 'brand',
    'type': 'type',
}
