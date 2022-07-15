from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response, status
from .serializers import AccessSerializer, AccessCreateSerializer, AccessUpdateSerializer
from main.models import Access_ad
from rest_framework.permissions import AllowAny

model_name = Access_ad

class AccessList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return model_name.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return model_name.objects.all()


class AccessDetails(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer


class AccessDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AccessSerializer


class AccessCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        result = AccessCreateSerializer.validate(self, data=request.data)
        return response.Response(result, status=status.HTTP_201_CREATED)


class AccessUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AccessUpdateSerializer

    def put(self, request, pk):
        AccessUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


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