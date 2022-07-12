from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response, status
from .serializers import MobileSerializer, MobileCreateSerializer, MobileUpdateSerializer
from main.models import Mobile_ad
from rest_framework.permissions import AllowAny

model_name = Mobile_ad


class MobileList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return model_name.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return model_name.objects.all()


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
    permission_classes = [AllowAny]

    def post(self, request):
        MobileCreateSerializer.validate(self, data=request.data)
        return response.Response(status=status.HTTP_201_CREATED)


class MobileUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = MobileUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        MobileUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


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
