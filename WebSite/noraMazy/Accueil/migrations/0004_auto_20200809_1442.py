# Generated by Django 3.0.8 on 2020-08-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accueil', '0003_auto_20200808_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='namePromo'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='photoPromo',
            field=models.ImageField(blank=True, null=True, upload_to='C:/Users/Professionnel/Desktop/EPHEC/TFE/WebSite/noraMazy/Accueil/media', verbose_name='photoPromo'),
        ),
    ]
