from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response, status
from .serializers import FurnitureSerializer, FurnitureCreateSerializer, FurnitureUpdateSerializer
from main.models import Furniture_ad
from rest_framework.permissions import AllowAny

model_name = Furniture_ad

class FurnitureList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return model_name.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return model_name.objects.all()


class FurnitureDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]


class FurnitureDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureSerializer


class FurnitureCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        FurnitureCreateSerializer.validate(self, data=request.data)
        return response.Response(status=status.HTTP_201_CREATED)


class FurnitureUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = FurnitureUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        FurnitureUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


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
