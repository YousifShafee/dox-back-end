from rest_framework.serializers import ModelSerializer
from main.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["images"]