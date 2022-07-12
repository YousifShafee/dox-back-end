from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Advertisement, Electronic_ad, Image, User


class ElectronicSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Electronic_ad
        fields = '__all__'

class ElectronicUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Electronic_ad
        fields = '__all__'
    
    def validate(self, data, pk):
        
        # Self Model (Electronic_ad)
        electronic_ad = Electronic_ad.objects.get(id=pk)
        electronic_ad.type=data['type']
        electronic_ad.condition=data['condition']
        electronic_ad.brand=data['brand']
        
        # Ad Model
        ad_id = Advertisement.objects.get(id=electronic_ad.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(ad_id.ad_image.id)
        ad_image.images=data['ad_image']
        
        ad_image.save()
        ad_id.save()
        electronic_ad.save()

        return data

class ElectronicCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Electronic_ad
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
        
        # Self Model (Electronic_ad)
        electronic_ad = Electronic_ad(
            ad_id=ad_id,
            type=data['type'],
            condition=data['condition'],
            brand=data['brand'],
        )
        
        ad_image.save()
        ad_id.save()
        electronic_ad.save()
        ad_id.product_id=electronic_ad.id
        ad_id.save()

        return data