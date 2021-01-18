# Generated by Django 3.1.5 on 2021-01-18 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='neighborhood_data',
            fields=[
                ('zipCode', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('crimeIndex', models.FloatField()),
                ('crimeCount', models.FloatField()),
                ('crimeRatio', models.FloatField()),
                ('neighborhood', models.CharField(blank=True, max_length=20, null=True)),
                ('quadrant', models.CharField(blank=True, max_length=10, null=True)),
                ('avgRent', models.FloatField(blank=True, null=True)),
                ('rentLow', models.FloatField(blank=True, null=True)),
                ('rentHigh', models.FloatField(blank=True, null=True)),
                ('walkIndex', models.FloatField(blank=True, null=True)),
                ('violenceIndex', models.FloatField(blank=True, null=True)),
                ('crimeTime', models.CharField(blank=True, max_length=2, null=True)),
                ('avgHomeValue', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='housing_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField()),
                ('projectName', models.CharField(max_length=100)),
                ('management', models.CharField(max_length=100)),
                ('xCoord', models.FloatField(blank=True, null=True)),
                ('yCoord', models.FloatField(blank=True, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=100)),
                ('contactPhone', models.CharField(max_length=12)),
                ('totalUnits', models.IntegerField(blank=True, null=True)),
                ('singleRoom', models.IntegerField(blank=True, null=True)),
                ('studio', models.IntegerField(blank=True, null=True)),
                ('oneBedroom', models.IntegerField(blank=True, null=True)),
                ('twoBedroom', models.IntegerField(blank=True, null=True)),
                ('threeBedroom', models.IntegerField(blank=True, null=True)),
                ('fourBedroom', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('zipCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing_app.neighborhood_data')),
            ],
            options={
                'ordering': ['projectName'],
            },
        ),
    ]
