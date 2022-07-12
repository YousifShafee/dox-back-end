from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer

from main.models import Advertisement, Image, Mobile, Mobile_ad, User

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

class MobileUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    mobile = MobileBrandSerializer(read_only=True)
    class Meta:
        model = Mobile
        fields = '__all__'
    
    def validate(self, data, pk):
        
        # Self Model (Car Rent)
        mobile_ad = Mobile_ad.objects.get(id=pk)
        mobile_ad.condition=data['condition']
        mobile_ad.payment=data['payment']
        # mobile_ad.warranty=data['warranty']

        # Mobile Model
        mobile = Mobile.objects.get(id=mobile_ad.mobile.id)
        mobile.brand=data['brand']
        mobile.type=data['type']
        
        # Ad Model
        ad_id = Advertisement.objects.get(id=mobile_ad.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(id=ad_id.ad_image.id)
        ad_image.images=data['ad_image']
        
        mobile.save()
        ad_image.save()
        ad_id.save()
        mobile_ad.save()

        return data

class MobileCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    mobile = MobileBrandSerializer(read_only=True)
    class Meta:
        model = Mobile
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

        # Mobile Model
        mobile = Mobile(
            brand=data['brand'],
            type=data['type'],
        )
        
        # Self Model (Car Rent)
        mobile_ad = Mobile_ad(
            ad_id=ad_id,
            mobile=mobile,
            condition=data['condition'],
            payment=data['payment'],
            # warranty=data['warranty'],
        )
        
        mobile.save()
        ad_image.save()
        ad_id.save()
        mobile_ad.save()
        ad_id.product_id=mobile_ad.id
        ad_id.save()

        return data