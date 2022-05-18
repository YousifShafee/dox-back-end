from django.db import models
from django.utils import timezone


class Super_User(models.Model):
    user_name = models.CharField(max_length=35)
    password = models.CharField(max_length=35)


class Vice_User(models.Model):
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    password = models.CharField(max_length=35)
    gender = models.CharField(max_length=35, choices=((("Male"), ("Male")), (("Female"), ("Female"))))
    mission = models.CharField(max_length=35, choices=((("Delete"), ("Delete")), (("Update"), ("Update")), (("All"), ("All"))))


class Normal_User(models.Model):
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    password = models.CharField(max_length=35)
    gender = models.CharField(max_length=10, choices=((("Male"), ("ذكر")), (("Female"), ("أنثى"))))


class Company(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    images = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=35)
    payment_no = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)


class Advertisement(models.Model):
    ad_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=15)
    ad_name = models.CharField(max_length=200)
    main_category = models.CharField(max_length=200)
    ad_description = models.CharField(max_length=200)
    person_name = models.CharField(max_length=200)
    ad_image = models.ImageField(upload_to="images/")
    created_date = models.DateTimeField(default=timezone.now)


class Payment_Ad(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


class Car_Rent(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    category = models.CharField(max_length=35)
    model = models.CharField(max_length=35)
    price = models.IntegerField()
    body_type = models.CharField(max_length=35)
    transmission_type = models.CharField(max_length=35)
    fuel_type = models.CharField(max_length=35)
    engine_capacity = models.CharField(max_length=35)
    rental_period = models.CharField(max_length=35)
    rental_option = models.CharField(max_length=35)


class Car_Sales(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    category = models.CharField(max_length=35)
    model = models.CharField(max_length=35)
    price = models.IntegerField()
    condition = models.CharField(max_length=35)
    color = models.CharField(max_length=35)
    year = models.DateField()
    kilometer = models.IntegerField()
    body_type = models.CharField(max_length=35)
    transmission_type = models.CharField(max_length=35)
    fuel_type = models.CharField(max_length=35)
    engine_capacity = models.CharField(max_length=35)
    extra_features = models.CharField(max_length=35, )
    ad_type = models.CharField(max_length=35)


class Properties_Rent(models.Model):
    property_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=35)
    compound = models.CharField(max_length=35)
    furnished = models.CharField(max_length=35)
    amenities = models.CharField(max_length=35)
    area = models.CharField(max_length=10)


class Properties_Sales(models.Model):
    property_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=35)
    compound = models.CharField(max_length=35)
    furnished = models.CharField(max_length=35)
    amenities = models.CharField(max_length=35)
    delivery_date = models.DateTimeField(default=timezone.now)
    delivery_term = models.CharField(max_length=35)
    payment = models.CharField(max_length=35)
    area = models.CharField(max_length=10)


class Medical_Supplies(models.Model):
    midical_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=35)
    condition = models.CharField(max_length=35)


class Electonic_ad(models.Model):
    electron_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=35)
    condition = models.CharField(max_length=35)
    brand = models.CharField(max_length=35)


class Mobile_ad(models.Model):
    mobile_id = models.CharField(max_length=200)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=35)
    condition = models.CharField(max_length=35)
    brand = models.CharField(max_length=35)
    payment = models.CharField(max_length=35)
    warranty = models.CharField(max_length=35)


class Access_ad(models.Model):
    access_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=35)
    condition = models.CharField(max_length=35)


class Furniture_ad(models.Model):
    furniture_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    department = models.CharField(max_length=10)
    condition = models.CharField(max_length=35)
    type = models.CharField(max_length=35)
