from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Properties, Properties_Rent, Properties_Sales


class PropertiesSerializer(ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'

class PropertiesRentSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Rent
        fields = '__all__'

class PropertiesSalesSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Sales
        fields = '__all__'
