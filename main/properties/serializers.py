from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Advertisement, Image, Properties, Properties_Rent, Properties_Sales, User


class PropertiesSerializer(ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'

class PropertiesRentSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Rent
        fields = '__all__'

class PropertiesRentUpdateSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Rent
        fields = '__all__'
    
    def validate(self, data, pk):
        
        # Self Model (Properties_Rent)
        properties_rent = Properties_Rent.objects.get(id=pk)

        # Properties Model
        properties = Properties.objects.get(id=properties_rent.properties.id)
        properties.bedroom=data['bedroom']
        properties.bathroom=data['bathroom']
        properties.type=data['type']
        # properties.furnished=data['furnished']
        properties.compound=data['compound']
        properties.area=data['area']
        
        # Ad Model
        ad_id = Advertisement.objects.get(id=properties_rent.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(id=ad_id.ad_image.id)
        ad_image.images=data['ad_image']
        
        ad_image.save()
        ad_id.save()
        properties.save()
        properties_rent.save()

        return data

class PropertiesRentCreateSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Rent
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

        # Properties Model
        properties = Properties(
            bedroom=data['bedroom'],
            bathroom=data['bathroom'],
            type=data['type'],
            # furnished=data['furnished'],
            compound=data['compound'],
            area=data['area'],
        )
        
        # Self Model (Car Rent)
        properties_rent = Properties_Rent(
            ad_id=ad_id,
            properties=properties,
        )
        
        ad_image.save()
        ad_id.save()
        properties.save()
        properties_rent.save()
        ad_id.product_id=properties_rent.id
        ad_id.save()

        return properties_rent


class PropertiesSalesSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Sales
        fields = '__all__'

class PropertiesSalesUpdateSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Sales
        fields = '__all__'
    
    def validate(self, data, pk):
        
        # Self Model (Car Sales)
        properties_sales = Properties_Sales.objects.get(id=pk)
        properties_sales.payment=data['payment']
        properties_sales.delivery_date=data['delivery_date']
        properties_sales.delivery_term=data['delivery_term']

        # Properties Model
        properties = Properties.objects.get(id=properties_sales.properties.id)
        properties.bedroom=data['bedroom']
        properties.bathroom=data['bathroom']
        properties.type=data['type']
        # properties.furnished=data['furnished']
        properties.compound=data['compound']
        properties.area=data['area']
        
        # Ad Model
        ad_id = Advertisement.objects.get(id=properties_sales.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(id=ad_id.ad_image.id)
        ad_image.images=data['ad_image']
        
        ad_image.save()
        ad_id.save()
        properties.save()
        properties_sales.save()

        return data

class PropertiesSalesCreateSerializer(ModelSerializer):
    properties = PropertiesSerializer(read_only=True)
    ad_id = AdSerializer(read_only=True)
    class Meta:
        model = Properties_Sales
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

        # Properties Model
        properties = Properties(
            bedroom=data['bedroom'],
            bathroom=data['bathroom'],
            type=data['type'],
            # furnished=data['furnished'],
            compound=data['compound'],
            area=data['area'],
        )
        
        # Self Model (Car Sales)
        properties_sales = Properties_Sales(
            ad_id=ad_id,
            properties=properties,
            payment=data['payment'],
            delivery_date=data['delivery_date'],
            delivery_term=data['delivery_term'],
        )
        
        ad_image.save()
        ad_id.save()
        properties.save()
        properties_sales.save()
        ad_id.product_id=properties_sales.id
        ad_id.save()

        return properties_sales