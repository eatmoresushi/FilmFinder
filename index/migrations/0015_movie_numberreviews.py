# Generated by Django 3.1.2 on 2020-11-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20201106_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='numberReviews',
            field=models.IntegerField(default=0),
        ),
    ]
