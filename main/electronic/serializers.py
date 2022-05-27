from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Electronic_ad


class ElectronicSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Electronic_ad
        fields = '__all__'
