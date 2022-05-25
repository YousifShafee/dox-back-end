from rest_framework.serializers import ModelSerializer


class AllDataSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
