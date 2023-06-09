# Generated by Django 2.2.5 on 2023-04-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20230411_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(blank=True, to='rooms.HouseRule'),
        ),
    ]
