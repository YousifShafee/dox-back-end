from rest_framework import generics
from datetime import date
from .serializers import ImageSerializer
from main.models import Image
from rest_framework.permissions import AllowAny

model_name = Image

class ImageList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        if 'category' in self.kwargs:
            if self.kwargs['category'] != 'without-ad':
                return model_name.objects.filter(category=self.kwargs['category']).order_by('-created_date')[:4]
            else:
                return model_name.objects.exclude(category=u'ad')
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
    # permission_classes = [IsAuthenticated]             TODO uncomment this line and remove previous

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())