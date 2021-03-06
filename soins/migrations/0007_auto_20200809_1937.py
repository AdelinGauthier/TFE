# Generated by Django 3.0.8 on 2020-08-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soins', '0006_fichesclients'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichesclients',
            name='Fidelite',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fichesclients',
            name='Histoire',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='fichesclients',
            name='Historique',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='fichesclients',
            name='Soins',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='soinsselect',
            name='extensionsCils',
            field=models.BooleanField(default=False, verbose_name='ExtentionsCils'),
        ),
    ]
