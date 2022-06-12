# Generated by Django 3.2.13 on 2022-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_modile_mobile_ad_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='access_ad',
            name='condition',
            field=models.CharField(choices=[('مستعمل', 'مستعمل'), ('جديد', 'جديد')], default='', max_length=35),
        ),
        migrations.AddField(
            model_name='access_ad',
            name='type',
            field=models.CharField(choices=[('احذية', 'احذية'), ('شنط', 'شنط'), ('نظارات', 'نظارات'), ('ملابس', 'ملابس'), ('ساعات', 'ساعات'), ('اخرى', 'اخرى')], default='', max_length=35),
        ),
        migrations.AddField(
            model_name='medical_ad',
            name='condition',
            field=models.CharField(choices=[('مستعمل', 'مستعمل'), ('جديد', 'جديد')], default='', max_length=35),
        ),
        migrations.AddField(
            model_name='medical_ad',
            name='type',
            field=models.CharField(choices=[('الاسنان', 'الاسنان'), ('العيون', 'العيون'), ('المطياف الضوئى', 'المطياف الضوئى'), ('حاضنة الاطفال', 'حاضنة الاطفال'), ('قياس الاكسجين', 'قياس الاكسجين'), ('الجراحة الكهربائى', 'الجراحة الكهربائى'), ('التنفس الصناعى', 'التنفس الصناعى'), ('غسيل كلوى', 'غسيل كلوى')], default='', max_length=35),
        ),
    ]
