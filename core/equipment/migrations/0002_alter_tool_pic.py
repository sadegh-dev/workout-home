# Generated by Django 4.1 on 2022-08-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='equipments/'),
        ),
    ]
