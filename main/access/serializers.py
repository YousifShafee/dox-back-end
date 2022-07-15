from rest_framework.serializers import ModelSerializer

from main.ad.serializers import AdSerializer
from main.models import Access_ad, Advertisement, Image, User


class AccessSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)

    class Meta:
        model = Access_ad
        fields = '__all__'


class AccessUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)

    class Meta:
        model = Access_ad
        fields = '__all__'

    def validate(self, data, pk):

        access_ad = Access_ad.objects.get(id=pk)
        # Self Model (Access_ad)
        access_ad.condition=data['condition']
        access_ad.type=data['type']

        # Image Model
        ad_image = Image.objects.get(id=access_ad.ad_id.ad_image.id)
        ad_image.images=data['ad_image']

        # Ad Model
        ad_id = Advertisement.objects.get(id=access_ad.ad_id.id)
        ad_id.ad_name=data['ad_name']
        ad_id.price=data['price']
        ad_id.description=data['description']        

        ad_image.save()
        ad_id.save()
        access_ad.save()

        return data


class AccessCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)

    class Meta:
        model = Access_ad
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
            ad_image=ad_image,
            user=User.objects.get(id=data['user']),
            ad_name=data['ad_name'],
            ad_type=data['ad_type'],
            price=data['price'],
            description=data['description'],
        )

        # Self Model (Access_ad)
        access_ad = Access_ad(
            ad_id=ad_id,
            condition=data['condition'],
            type=data['type'],
        )

        ad_image.save()
        ad_id.save()
        access_ad.save()
        ad_id.product_id=access_ad.id
        ad_id.save()

        return access_ad
