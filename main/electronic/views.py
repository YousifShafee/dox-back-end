from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response, status
from .serializers import ElectronicSerializer, ElectronicCreateSerializer, ElectronicUpdateSerializer
from main.models import Electronic_ad
from rest_framework.permissions import AllowAny

model_name = Electronic_ad

class ElectronicList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return model_name.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return model_name.objects.all()


class ElectronicDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [AllowAny]


class ElectronicDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ElectronicSerializer


class ElectronicCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        result = ElectronicCreateSerializer.validate(self, data=request.data)
        return response.Response(result, status=status.HTTP_201_CREATED)


class ElectronicUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ElectronicUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        ElectronicUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


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
