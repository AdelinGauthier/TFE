# Generated by Django 3.0.8 on 2020-08-08 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soins', '0003_auto_20200808_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='soinsselect',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='soinsselect',
            name='extensionsCils',
            field=models.BooleanField(default=False),
        ),
    ]
