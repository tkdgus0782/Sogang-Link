# Generated by Django 4.2.11 on 2024-04-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_alter_notice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]