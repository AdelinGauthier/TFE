# Generated by Django 3.0.5 on 2020-08-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accueil', '0004_auto_20200809_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254)),
                ('email', models.CharField(blank=True, max_length=254)),
                ('msg', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
