# Generated by Django 3.0.8 on 2020-08-09 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200809_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='Client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.ClientsList'),
        ),
    ]
