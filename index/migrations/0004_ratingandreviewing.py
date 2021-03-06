# Generated by Django 3.1.1 on 2020-10-15 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0003_auto_20201014_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingAndReviewing',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('review', models.CharField(default='', max_length=500)),
                ('ifrate', models.IntegerField(default=0)),
                ('ifreview', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='index.movie')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
