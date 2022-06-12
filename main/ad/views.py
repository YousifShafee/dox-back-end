from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, status, views, response
from .serializers import *
from main.models import Advertisement, Image, User
from rest_framework.permissions import AllowAny, IsAuthenticated

model_name = Advertisement

class AdList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return model_name.objects.filter(user__id=self.kwargs['user_id'])
        else:
            return model_name.objects.all()


class AdDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]


class AdDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = AdSerializer


class AdCreate(generics.CreateAPIView):
    queryset = model_name.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]             TODO uncomment this line and remove previous
    serializer_class = AdSerializer

    def post(self, request):
        image = Image(
            images=request.data['image'],
            category='ad'
            )
        image.save()
        user = User.objects.get(email=request.data['email'])
        ad = Advertisement(
            ad_image=image,
            user=user,
            ad_name=request.data['ad_name'],
            description=request.data['description'],
        )
        ad.save()
        return response.Response(status=status.HTTP_201_CREATED)


class AdUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]             TODO uncomment this line and remove previous

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class ActiveAdUpdate(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ActiveAdSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]             TODO uncomment this line and remove previous

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class AdSearch(views.APIView):
    queryset = model_name.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = model_name.objects.filter(**q)
        result = AdSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'payment_n': 'payment_n__contains',
    'ad_name': 'ad_name__contains',
    'price': 'price__range',
}