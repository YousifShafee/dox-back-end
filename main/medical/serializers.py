from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Advertisement, Medical_ad, Image, User


class MedicalSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Medical_ad
        fields = '__all__'

class MedicalUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Medical_ad
        fields = '__all__'
    
    def validate(self, data, pk):

        # Medical_ad Model
        medical_ad = Medical_ad.objects.get(id=pk)
        medical_ad.condition=data['condition']
        medical_ad.type=data['type']
        
        # Ad Model
        ad_id = Advertisement.objects.get(id=medical_ad.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(id=ad_id.ad_image.id)
        ad_image.images=data['ad_image']
        
        ad_image.save()
        ad_id.save()
        medical_ad.save()

        return data

class MedicalCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Medical_ad
        fields = '__all__'
    
    def validate(self, data):

        # Image Model
        ad_image = Image(
            images=data['ad_image'],
            user=User.objects.get(id=data['user']),
            category='ad',
        )
        
        # Ad Model
        ad_id = Advertisement(
            ad_image = ad_image,
            user=User.objects.get(id=data['user']),
            ad_name = data['ad_name'],
            ad_type = data['ad_type'],
            price = data['price'],
            description = data['description'],
        )

        # Medical_ad Model
        medical_ad = Medical_ad(
            ad_id=ad_id,
            condition=data['condition'],
            type=data['type'],
        )
        
        ad_image.save()
        ad_id.save()
        medical_ad.save()
        ad_id.product_id=medical_ad.id
        ad_id.save()

        return data