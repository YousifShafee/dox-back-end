from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Car_Rent


class MedicalSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Car_Rent
        fields = '__all__'
