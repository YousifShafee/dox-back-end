from rest_framework import generics
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
            return model_name.objects.filter(category=self.kwargs['category']).order_by('created_date')[:6]
        else:
            return model_name.objects.all().order_by('created_date')[:6]
