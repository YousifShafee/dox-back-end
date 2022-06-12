from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response
from .serializers import AccessSerializer
from main.models import Access_ad
from rest_framework.permissions import AllowAny

model_name = Access_ad

class AccessList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer


class AccessDetails(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer


class AccessDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer


class AccessCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class AccessUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class AccessSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = AccessSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'price': 'ad_id__price__range',
    'type': 'type',
    'condition': 'condition',
}