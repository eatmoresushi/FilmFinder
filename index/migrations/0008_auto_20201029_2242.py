# Generated by Django 3.1.2 on 2020-10-29 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20201029_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratedreview',
            old_name='rate',
            new_name='rating',
        ),
    ]
