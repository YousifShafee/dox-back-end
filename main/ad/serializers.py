from rest_framework.serializers import ModelSerializer
from main.models import Advertisement
from main.image.serializers import ImageSerializer
from main.user.serializers import UsersSerializer


class AdSerializer(ModelSerializer):
    ad_image = ImageSerializer(read_only=True)
    user = UsersSerializer(read_only=True)
    
    class Meta:
        model = Advertisement
        fields = '__all__'