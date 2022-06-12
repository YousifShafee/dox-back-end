from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response
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


class FurnitureSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = FurnitureSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'price': 'ad_id__price__range',
    'condition': 'condition',
    'type': 'type',
    'department': 'department__name',
}
