# Generated by Django 3.2.13 on 2022-05-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220524_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=35)),
                ('password', models.CharField(default='', max_length=35)),
                ('phone', models.CharField(default='', max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'ذكر'), ('Female', 'أنثى')], default='', max_length=35)),
                ('mission', models.CharField(choices=[('Delete', 'مسح'), ('Update', 'تعديل'), ('Admin', 'ادمن')], default='Update', max_length=35)),
            ],
        ),
        migrations.DeleteModel(
            name='Super_User',
        ),
        migrations.DeleteModel(
            name='Vice_User',
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('general', 'عام'), ('featur_car', 'شركات مميزة سيارات'), ('car_sale', 'سيارات للبيع'), ('car_rent', 'سيارات للإيجار'), ('featur_property', 'شركات مميزة عقارات'), ('property_sale', 'عقارات للبيع'), ('property_rent', 'عقارات للإيجار'), ('featur_mobile', 'شركات مميزة موبايل'), ('mobile', 'موبايلات'), ('featur_access', 'شركات مميزة اكسسوارات'), ('access', 'إكسسوارات'), ('featur_midical', 'شركات مميزة طبية'), ('midical', 'مستلزمات طبية'), ('featur_electron', 'شركات مميزة إلكترونيات'), ('electron', 'إكترونيات وأجهزة منزلية'), ('featur_furniture', 'شركات مميزة أثاث'), ('furniture', 'أثاث منزلي')], default='', max_length=35),
        ),
    ]
