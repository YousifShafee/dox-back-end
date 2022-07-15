from rest_framework.serializers import ModelSerializer
from main.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ActiveImageSerializer(ModelSerializer):    
    class Meta:
        model = Image
        fields = ['is_active']

class ImageUpdateSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['images']