# Generated by Django 4.1 on 2022-08-21 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_the_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='the_link',
        ),
    ]