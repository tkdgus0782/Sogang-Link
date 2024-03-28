# Generated by Django 4.2.11 on 2024-03-28 03:25

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, null=True)),
                ('semester', models.IntegerField()),
                ('name', models.CharField(max_length=30, null=True)),
                ('day', models.IntegerField()),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('classroom', models.CharField(default='', max_length=15)),
                ('advisor', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod', models.IntegerField()),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=100, null=True)),
                ('url', models.URLField(null=True)),
                ('writer', models.CharField(max_length=100, null=True)),
                ('file', models.URLField(null=True)),
                ('date', models.DateField()),
                ('view', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_grade', models.FloatField(null=True)),
                ('final_grade', models.FloatField(null=True)),
                ('real', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='takes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]