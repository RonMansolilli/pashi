# Generated by Django 3.1.5 on 2021-01-16 01:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('housing_app', '0002_auto_20210115_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing_data',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
