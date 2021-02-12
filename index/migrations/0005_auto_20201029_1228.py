# Generated by Django 3.1.2 on 2020-10-29 12:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0004_ratingandreviewing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingandreviewing',
            name='ifrate',
        ),
        migrations.RemoveField(
            model_name='ratingandreviewing',
            name='ifreview',
        ),
        migrations.AddField(
            model_name='movie',
            name='avgRating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ratingandreviewing',
            name='cDate',
            field=models.DateField(
                default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ratingandreviewing',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ratingandreviewing',
            name='review',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='banlist',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('blockedUser', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
