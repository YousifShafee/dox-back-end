from datetime import date
from rest_framework import generics, views, response, status
from .serializers import MedicalSerializer, MedicalCreateSerializer, MedicalUpdateSerializer
from main.models import Medical_ad
from main.general_fun import get_data_by_field
from rest_framework.permissions import AllowAny

model_name = Medical_ad

class MedicalList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return model_name.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return model_name.objects.all()


class MedicalDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [AllowAny]


class MedicalDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalSerializer


class MedicalCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        MedicalCreateSerializer.validate(self, data=request.data)
        return response.Response(status=status.HTTP_201_CREATED)


class MedicalUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MedicalUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        MedicalUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


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