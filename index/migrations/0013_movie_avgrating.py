# Generated by Django 3.1.2 on 2020-11-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avgRating',
            field=models.FloatField(default=0),
        ),
    ]
