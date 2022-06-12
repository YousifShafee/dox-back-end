from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response
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


class MobileSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = MobileSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'condition': 'condition',
    'price': 'ad_id__price__range',
    'brand': 'mobile__brand',
    'type': 'mobile__type',
    'payment': 'payment',
    'warranty': 'warranty',
}
