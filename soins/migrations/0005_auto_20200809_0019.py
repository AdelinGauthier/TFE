# Generated by Django 3.0.8 on 2020-08-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soins', '0004_auto_20200808_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soinsselect',
            old_name='teinture',
            new_name='teintureCils',
        ),
        migrations.AddField(
            model_name='soinsselect',
            name='teintureSourcils',
            field=models.BooleanField(default=False),
        ),
    ]
