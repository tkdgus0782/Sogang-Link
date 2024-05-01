# Generated by Django 4.2.11 on 2024-05-01 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('facilities', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('open_hours', models.CharField(blank=True, max_length=100, null=True)),
                ('total_seats', models.IntegerField(blank=True, null=True)),
                ('available_seats', models.IntegerField(blank=True, null=True)),
                ('facility_type', models.CharField(max_length=100)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility', to='maps.building')),
            ],
        ),
    ]