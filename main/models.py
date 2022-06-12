from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from multiselectfield import MultiSelectField
from django.utils import timezone
from .choices import *


class UserManager(BaseUserManager):
    def create_user(self, username=None, password=None):
        if not username:
            raise ValueError('User must have an Username')
        user = self.model(username=username)
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_vice_delete(self, username=None, password=None):
        user = self.create_user(username,password=password)
        user.mission = "Delete"
        user.admin = False
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_vice_update(self, username=None, password=None):
        user = self.create_user(username,password=password)
        user.mission = "Update"
        user.admin = False
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_normal(self, username=None, password=None):
        user = self.create_user(username=username,password=password)
        user.mission = "Normal"
        user.admin = False
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username=None, password=None):
        user = self.create_user(username=username,password=password)
        user.mission = "Admin"
        user.admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=15, default='')
    first_name = models.CharField(max_length=15, default='')
    last_name = models.CharField(max_length=15, default='')
    gender = models.CharField(max_length=10, choices=gender_type, default='')
    mission = models.CharField(max_length=35, choices=action_level, default='Normal')
    active_code = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_module_perms(self, app_label):
        if self.mission == "Admin":
            return True
        return False
    
    def has_perm(self, perm, obj=None):
        if self.mission == "Admin":
            return True
        return False
    
    def get_username(self):
        if self.username:
            return self.username
        return self.username

    def get_password(self):
        if self.password:
            return self.password
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        if self.mission == "Admin":
            return True
        return False

    def __str__(self):
        return self.username


class Image(models.Model):
    images = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=35, default='', choices=image_category)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.category + ' - ' + str(self.images)


class Advertisement(models.Model):
    ad_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_name = models.CharField(max_length=200, default='')
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=4096, default='')
    payment_n = models.CharField(max_length=200, default='', blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.email) + ' - ' + self.ad_name


class Car_Brand(models.Model):
    brand = models.CharField(max_length=35, choices=car_brand, default='')
    model = models.CharField(max_length=35, default='')
    
    def __str__(self):
        return self.brand + ' - ' + self.model


class Car(models.Model):
    body_type = models.CharField(max_length=35, default='', choices=body_c)
    brand = models.ForeignKey(Car_Brand, on_delete=models.CASCADE, null=True)
    fuel_type = models.CharField(max_length=35, default='', choices=fuel_c)
    engine_capacity = models.IntegerField(default=0)
    year = models.DateField()
    color = models.CharField(max_length=35, default='', choices=color_c)
    transmission_type = models.CharField(max_length=35, default='', choices=transmission_c)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    extra_features = MultiSelectField(choices=extra_c)
    
    def __str__(self):
        return str(self.brand) + ' - ' + str(self.year.year)


class Car_Rent(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    rental_period = models.CharField(max_length=20, choices=rental_period_c, default='')
    rental_option = models.CharField(max_length=15, default='', choices=rental_option_c)
    
    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.car)


class Car_Sales(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    kilometer = models.IntegerField(default=0)
    ad_type = models.CharField(max_length=35, default='', choices=sale_or_rent)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.car)


class Properties(models.Model):
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    type = models.CharField(max_length=35, default='', choices=properties_type_c)
    furnished = models.BooleanField(default=False)
    compound = models.CharField(max_length=35, default='', choices=compound_c)
    amenities = MultiSelectField(choices=amenities_c)
    
    area = models.IntegerField(default=100)

    def __str__(self):
        return self.type + ' - ' + self.compound


class Properties_Rent(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    properties = models.ForeignKey(Properties, on_delete=models.CASCADE)

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
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    payment = models.CharField(max_length=35, default='', choices=payment_c)
    warranty = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.mobile)


class Access_ad(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    type = models.CharField(max_length=35, default='', choices=access_type_c)

    def __str__(self):
        return str(self.ad_id)

class Medical_ad(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    condition = models.CharField(max_length=35, default='', choices=condition_c)
    type = models.CharField(max_length=35, default='', choices=medical_type_c)

    def __str__(self):
        return str(self.ad_id)

class Department(models.Model):
    name = models.CharField(max_length=35, default='', choices=department_name_c)
    attach = models.CharField(max_length=35, default='')

    def __str__(self):
        return self.name + ' - ' + self.attach


class Furniture_ad(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    condition = models.CharField(max_length=35, default='', choices=condition_c)

    def __str__(self):
        return str(self.ad_id) + ' - ' + str(self.department)
