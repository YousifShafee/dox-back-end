from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Advertisement, Department, Furniture_ad, Image, User


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


class FurnitureUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = Furniture_ad
        fields = '__all__'
    
    def validate(self, data, pk):

        furniture_ad = Furniture_ad.objects.get(id=pk)
        furniture_ad.condition=data['condition']

        ad_image = Image.objects.get(id=furniture_ad.ad_id.ad_image.id)
        ad_image.images=data['ad_image']

        ad_id = Advertisement.objects.get(id=furniture_ad.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        department = Department.objects.get(id=furniture_ad.department.id)
        department.name=data['name']
        department.attach=data['attach']

        ad_image.save()
        ad_id.save()
        department.save()
        furniture_ad.save()


class FurnitureCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = Furniture_ad
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

        department = Department(
            name=data['name'],
            attach=data['attach'],
        )
        
        # Self Model (Furniture_ad)
        furniture_ad = Furniture_ad(
            ad_id=ad_id,
            department=department,
            condition=data['condition']
        )
        
        ad_image.save()
        ad_id.save()
        department.save()
        furniture_ad.save()
        ad_id.product_id=furniture_ad.id
        ad_id.save()

        return furniture_ad