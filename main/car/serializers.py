from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Car, Car_Brand, Car_Rent, Car_Sales


class CarBrandSerializer(ModelSerializer):
    class Meta:
        model = Car_Brand
        fields = '__all__'

class CarSerializer(ModelSerializer):
    brand = CarBrandSerializer(read_only=True)
    class Meta:
        model = Car
        fields = '__all__'

class CarSalesSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Sales
        fields = '__all__'

class CarRentSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Rent
        fields = '__all__'
