from main.general_fun import get_data_by_field
from rest_framework import generics, views, response
from datetime import date
from .serializers import *
from main.models import Image
from rest_framework.permissions import AllowAny

model_name = Image

class ImageList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        if 'category' in self.kwargs:
            if self.kwargs['category'] == 'without-ad':
                return model_name.objects.exclude(category=u'ad')
            elif self.kwargs['category'] == 'without-ad-logo-general':
                return model_name.objects.exclude(category__in=['ad', 'general', 'logo'])
            else:
                return model_name.objects.filter(category=self.kwargs['category']).order_by('-created_date')[:4]
        else:
            return model_name.objects.all().order_by('-created_date')[:4]

class ImageCreateAPIView(generics.CreateAPIView):
    queryset = model_name.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save()


class ImageDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]


class ImageUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class ActiveImageUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ActiveImageSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class ImageSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = ImageSerializer(model_data, many=True).data
        return response.Response(result)

search_dict = {
    'payment_n': 'payment_n__contains'
}