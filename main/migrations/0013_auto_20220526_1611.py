# Generated by Django 3.2.13 on 2022-05-26 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220526_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_rent',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='car_rent',
            name='type',
        ),
        migrations.AddField(
            model_name='car_rent',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.car'),
        ),
        migrations.AddField(
            model_name='car_rent',
            name='rental_option',
            field=models.CharField(choices=[('advance', 'مقدم'), ('late', 'مأخر')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='car_rent',
            name='rental_period',
            field=models.CharField(choices=[('year', 'سنوى'), ('month', 'شهرى'), ('day', 'يومى')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='price',
            field=models.CharField(choices=[('30000 - 100000', '30000 - 100000'), ('100000 - 300000', '100000 - 300000'), ('300000 - 500000', '300000 - 500000'), ('500000 - 1000000', '500000 - 1000000'), ('1000000 - 5000000', '1000000 - 5000000')], default='', max_length=20),
        ),
    ]