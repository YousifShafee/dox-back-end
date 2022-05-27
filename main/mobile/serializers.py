from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer

from main.models import Mobile, Mobile_ad

class MobileBrandSerializer(ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'

class MobileSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    mobile = MobileBrandSerializer(read_only=True)
    class Meta:
        model = Mobile_ad
        fields = '__all__'