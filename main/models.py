from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from multiselectfield import MultiSelectField
from django.utils import timezone
from .choices import *


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, default='')
    first_name = models.CharField(max_length=15, default='')
    last_name = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=35, default='')
    gender = models.CharField(max_length=10, choices=gender_type, default='')
    mission = models.CharField(max_length=35, choices=action_level, default='Normal')
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    # objects = UserManager()

    def __str__(self):
        return self.first_name + ' - ' + self.last_name


class Image(models.Model):
    images = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=35, default='', choices=image_category)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.category + ' - ' + self.created_date.strftime("%m-%d %M:%S")


class Advertisement(models.Model):
    ad_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_name = models.CharField(max_length=200, default='')
    ad_type = models.CharField(choices=sale_or_rent, max_length=25, default='')
    amount = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user) + ' - ' + self.ad_name


class Car_Brand(models.Model):
    brnad = models.CharField(max_length=35, choices=car_brand, default='')
    model = models.CharField(max_length=35, default='')
    
    def __str__(self):
        return self.brnad + ' - ' + self.model


class Car(models.Model):
    body_type = models.CharField(max_length=35, default='', choices=body_c)
    brand = models.ForeignKey(Car_Brand, on_delete=models.CASCADE, null=True)
    fuel_type = models.CharField(max_length=35, default='', choices=fuel_c)
    engine_capacity = models.CharField(max_length=35, default='', choices=engin_c)
    year = models.DateField()
    color = models.CharField(max_length=35, default='', choices=color_c)
    transmission_type = models.CharField(max_length=35, default='', choices=transmission_c)
    extra_features = MultiSelectField(choices=extra_c)
    
    def __str__(self):
        return str(self.brnad) + ' - ' + self.year


class Car_Rent(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=20, default='', choices=car_price)
    rental_period = models.CharField(max_length=20, choices=rental_period_c, default='')
    rental_option = models.CharField(max_length=15, default='', choices=rental_option_c)
    
    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.car)


class Car_Sales(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.CharField(max_length=20, default='', choices=car_price)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    kilometer = models.CharField(max_length=35, default='', choices=kilometer_c)
    ad_type = models.CharField(max_length=35, default='', choices=sale_or_rent)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.car)


class Properties(models.Model):
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    price = models.CharField(max_length=20, default='', choices=properties_price)
    type = models.CharField(max_length=35, default='', choices=properties_type_c)
    furnished = models.BooleanField(default=False)
    compound = models.CharField(max_length=35, default='', choices=compound_c)
    amenities = models.CharField(max_length=35, default='', choices=amenities_c)
    area = models.IntegerField(default=100)

    def __str__(self):
        return self.type + ' - ' + self.compound


class Properties_Rent(models.Model):
    properties = models.ForeignKey(Properties, on_delete=models.CASCADE)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.properties)


class Properties_Sales(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    properties = models.ForeignKey(Properties, on_delete=models.CASCADE)
    payment = models.CharField(max_length=35, default='', choices=payment_c)
    delivery_date = models.DateTimeField(default=timezone.now)
    delivery_term = models.CharField(max_length=35, default='', choices=delivery_term_c)
    
    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.properties)


class Electronic_ad(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.CharField(max_length=15, default='', choices=electronic_price_c)
    type = models.CharField(max_length=35, default='', choices=electronic_type_c)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    brand = models.CharField(max_length=35, default='', choices=electronic_brand_c)

    def __str__(self):
        return str(self.ad_id) + ' - ' + self.type


class Mobile(models.Model):
    brand = models.CharField(max_length=200, default='', choices=mobile_brand_c)
    type = models.CharField(max_length=35, default='')

    def __str__(self):
        return self.brand + ' - ' + self.type


class Mobile_ad(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    modile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    price = models.CharField(max_length=15, default='', choices=modile_price_c)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    payment = models.CharField(max_length=35, default='', choices=payment_c)
    warranty = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.modile)


class Department(models.Model):
    name = models.CharField(max_length=35, default='', choices=department_name_c)
    attach = models.CharField(max_length=35, default='')

    def __str__(self):
        return self.name + ' - ' + self.attach


class Furniture_ad(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.CharField(max_length=15, default='', choices=furniture_price_c)
    condition = models.CharField(max_length=35, default='', choices=condition_c)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.department)
