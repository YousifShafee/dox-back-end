from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Department, Furniture_ad


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class FurnitureSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = Furniture_ad
        fields = '__all__'