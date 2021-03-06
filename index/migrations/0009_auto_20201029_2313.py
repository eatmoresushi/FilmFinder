# Generated by Django 3.1.2 on 2020-10-29 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0008_auto_20201029_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratedreview',
            name='movie',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='index.movie'),
        ),
        migrations.AlterField(
            model_name='ratedreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
