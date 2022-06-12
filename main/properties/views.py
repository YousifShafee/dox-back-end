from main.general_fun import get_data_by_field
from datetime import date
from rest_framework import generics, views, response
from .serializers import PropertiesRentSerializer, PropertiesSalesSerializer
from main.models import Properties_Rent, Properties_Sales
from rest_framework.permissions import AllowAny


class PropertiesSalesList(generics.ListAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer
    permission_classes = [AllowAny]


class PropertiesSalesDetails(generics.RetrieveAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer
    permission_classes = [AllowAny]


class PropertiesSalesDelete(generics.DestroyAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer


class PropertiesSalesCreate(generics.CreateAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class PropertiesSalesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class PropertiesSalesSearch(views.APIView):
    queryset = Properties_Sales.objects.all()
    serializer_class = PropertiesSalesSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = Properties_Sales.objects.filter(**q)
        result = PropertiesSalesSerializer(model_data, many=True).data
        return response.Response(result)


class PropertiesRentList(generics.ListAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer
    permission_classes = [AllowAny]


class PropertiesRentDetails(generics.RetrieveAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer
    permission_classes = [AllowAny]


class PropertiesRentDelete(generics.DestroyAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer


class PropertiesRentCreate(generics.CreateAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class PropertiesRentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=date.today())


class PropertiesRentSearch(views.APIView):
    queryset = Properties_Rent.objects.all()
    serializer_class = PropertiesRentSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = Properties_Rent.objects.filter(**q)
        result = PropertiesRentSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'bathroom': 'properties__bathroom ',
    'bedroom': 'properties__bedroom ',
    'type': 'properties__type ',
    'compound': 'properties__compound',
    'furnished': 'properties__furnished',
    'area': 'properties__area',
    'delivery_date': 'delivery_date',
    'delivery_term': 'delivery_term',
    'payment': 'payment',
    'price': 'ad_id__price__range',
    'amenities': 'properties__amenities',
}
