# Generated by Django 3.0.8 on 2020-08-09 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200809_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientslist',
            name='clients',
        ),
        migrations.AddField(
            model_name='clientslist',
            name='clientsName',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='Client',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.ClientsList'),
        ),
    ]
