from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class MobileResource(resources.ModelResource):
    class Meta:
        model = Mobile

class MobileAdmin(ImportExportModelAdmin):
    resource_class = MobileResource

class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

class ImageAdmin(ImportExportModelAdmin):
    resource_class = ImageResource

class Car_BrandResource(resources.ModelResource):
    class Meta:
        model = Car_Brand

class Car_BrandAdmin(ImportExportModelAdmin):
    resource_class = Car_BrandResource

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department

class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource


admin.site.register(User)
admin.site.register(Advertisement)
admin.site.register(Medical_ad)
admin.site.register(Car)
admin.site.register(Car_Rent)
admin.site.register(Car_Sales)
admin.site.register(Properties)
admin.site.register(Properties_Rent)
admin.site.register(Properties_Sales)
admin.site.register(Electronic_ad)
admin.site.register(Mobile_ad)
admin.site.register(Access_ad)
admin.site.register(Furniture_ad)

admin.site.register(Car_Brand, Car_BrandAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Mobile, MobileAdmin)
admin.site.register(Image, ImageAdmin)