# Generated by Django 2.1.7 on 2019-05-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_auto_20190503_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(upload_to='foto'),
        ),
    ]
