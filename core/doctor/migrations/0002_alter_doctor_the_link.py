# Generated by Django 4.1 on 2022-08-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='the_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]