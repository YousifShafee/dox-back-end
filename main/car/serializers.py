from rest_framework.serializers import ModelSerializer
from main.ad.serializers import AdSerializer
from main.models import Advertisement, Car, Car_Brand, Car_Rent, Car_Sales, Image, User


class CarBrandSerializer(ModelSerializer):
    class Meta:
        model = Car_Brand
        fields = '__all__'

class CarSerializer(ModelSerializer):
    brand = CarBrandSerializer(read_only=True)
    class Meta:
        model = Car
        fields = '__all__'

class CarSalesSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Sales
        fields = '__all__'

class CarSalesUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Sales
        fields = '__all__'
    
    def validate(self, data, pk):
        
        # Self Model (Car Sales)
        car_sales = Car_Sales.objects.get(id=pk)
        car_sales.kilometer=data['kilometer']
        car_sales.offer_type=data['offer_type']
        
        # Ad Model
        ad_id = Advertisement.objects.get(id=car_sales.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(id=ad_id.ad_image.id)
        ad_image.images=data['ad_image']

        # Car Model
        car = Car.objects.get(id=car_sales.car.id)
        car.body_type = data['body_type']
        car.fuel_type = data['fuel_type']
        car.engine_capacity = data['engine_capacity']
        car.year = data['year']
        car.color = data['color']
        car.transmission_type = data['transmission_type']
        car.condition = data['condition']
        

        # Car Brand
        brand = Car_Brand.objects.get(id=car.brand.id)
        brand.brand=data['brand']
        brand.model=data['model']
        
        brand.save()
        ad_image.save()
        ad_id.save()
        car.save()
        car_sales.save()

        return data

class CarSalesCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Sales
        fields = '__all__'
    
    def validate(self, data):
                
        # Car Brand
        brand = Car_Brand(
            brand=data['brand'],
            model=data['model']
        )

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

        # Car Model
        car = Car(
            body_type = data['body_type'],
            brand=brand,
            fuel_type = data['fuel_type'],
            engine_capacity = data['engine_capacity'],
            year = data['year'],
            color = data['color'],
            transmission_type = data['transmission_type'],
            condition = data['condition'],
        )
        
        # Self Model (Car Sales)
        car_sales = Car_Sales(
            ad_id=ad_id,
            car=car,
            kilometer=data['kilometer'],
            offer_type=data['offer_type'],
        )

        brand.save()
        ad_image.save()
        ad_id.save()
        car.save()
        car_sales.save()
        ad_id.product_id=car_sales.id
        ad_id.save()

        return car_sales


class CarRentSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Rent
        fields = '__all__'


class CarRentUpdateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Rent
        fields = '__all__'
    
    def validate(self, data, pk):
        
        # Self Model (Car Rent)
        car_rent = Car_Rent.objects.get(id=pk)
        car_rent.rental_period=data['rental_period']
        car_rent.rental_option=data['rental_option']

        # Car Brand
        brand = Car_Brand.objects.get(car_rent.car.brand.id)
        brand.brand=data['brand']
        brand.model=data['model']

        
        # Ad Model
        ad_id = Advertisement.objects.get(id=car_rent.ad_id.id)
        ad_id.ad_name = data['ad_name']
        ad_id.ad_type = data['ad_type']
        ad_id.price = data['price']
        ad_id.description = data['description']

        # Image Model
        ad_image = Image.objects.get(id=ad_id.ad_image.id)
        ad_image.images=data['ad_image']

        # Car Model
        car = Car.objects.get(id=car_rent.car.id)
        car.body_type = data['body_type']
        car.fuel_type = data['fuel_type']
        car.engine_capacity = data['engine_capacity']
        car.transmission_type = data['transmission_type']

        brand.save()
        ad_image.save()
        ad_id.save()
        car.save()
        car_rent.save()

        return data


class CarRentCreateSerializer(ModelSerializer):
    ad_id = AdSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    class Meta:
        model = Car_Rent
        fields = '__all__'
    
    def validate(self, data):
                
        # Car Brand
        brand = Car_Brand(
            brand=data['brand'],
            model=data['model']
        )

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

        # Car Model
        car = Car(
            body_type = data['body_type'],
            fuel_type = data['fuel_type'],
            brand=brand,
            engine_capacity = data['engine_capacity'],
            transmission_type = data['transmission_type'],
        )
        
        # Self Model (Car Rent)
        car_rent = Car_Rent(
            ad_id=ad_id,
            car=car,
            rental_period=data['rental_period'],
            rental_option=data['rental_option'],
        )
        
        brand.save()
        ad_image.save()
        ad_id.save()
        car.save()
        car_rent.save()
        ad_id.product_id=car_rent.id
        ad_id.save()

        return car_rent