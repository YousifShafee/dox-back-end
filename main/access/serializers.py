from rest_framework.serializers import ModelSerializer

from main.ad.serializers import AdSerializer
from main.models import Access_ad

    
class AccessSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Access_ad
        fields = '__all__'
