from main.general_fun import get_data_by_field
from datetime import date
from rest_framework.permissions import AllowAny
from rest_framework import generics, views, response, status
from .serializers import CarSalesSerializer, CarRentSerializer, CarSalesCreateSerializer, CarRentCreateSerializer, CarRentUpdateSerializer, CarSalesUpdateSerializer
from main.models import Car_Rent, Car_Sales


class CarSalesList(generics.ListAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return Car_Sales.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return Car_Sales.objects.all()


class CarSalesDetails(generics.RetrieveAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer
    permission_classes = [AllowAny]


class CarSalesDelete(generics.DestroyAPIView):
    queryset = Car_Sales.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CarSalesSerializer


class CarSalesCreate(generics.CreateAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        result = CarSalesCreateSerializer.validate(self, data=request.data)
        return response.Response({result.id}, status=status.HTTP_201_CREATED)


class CarSalesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        CarSalesUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


class CarSalesSearch(views.APIView):
    queryset = Car_Sales.objects.all()
    serializer_class = CarSalesSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = Car_Sales.objects.filter(**q)
        result = CarSalesSerializer(model_data, many=True).data
        return response.Response(result)


class CarRentList(generics.ListAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return Car_Rent.objects.filter(ad_id__user__id=self.kwargs['user_id'])
        else:
            return Car_Rent.objects.all()


class CarRentDetails(generics.RetrieveAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer
    permission_classes = [AllowAny]


class CarRentDelete(generics.DestroyAPIView):
    queryset = Car_Rent.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CarRentSerializer


class CarRentCreate(generics.CreateAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        result = CarRentCreateSerializer.validate(self, data=request.data)
        return response.Response({result.id}, status=status.HTTP_201_CREATED)


class CarRentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        CarRentUpdateSerializer.validate(self, data=request.data, pk=pk)
        return response.Response(status=status.HTTP_200_OK)


class CarRentSearch(views.APIView):
    queryset = Car_Rent.objects.all()
    serializer_class = CarRentSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        model_data = Car_Rent.objects.filter(**q)
        result = CarRentSerializer(model_data, many=True).data
        return response.Response(result)


search_dict = {
    'brand': 'car__brand__brand',
    'model': 'car__brand__model',
    'price': 'ad_id__price__range',
    'condition': 'car__condition',
    'color': 'car__color',
    'year': 'car__year',
    'kilometer': 'kilometer',
    'transmission_type': 'car__transmission_type',
    'fuel_type': 'car__fuel_type',
    'engine_capacity': 'car__engine_capacity',
    'offer_type': 'offer_type',
    'body_type': 'car__body_type',
    'rental_option': 'car__rental_option',
    'rental_period': 'car__rental_period',
}