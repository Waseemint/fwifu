# Generated by Django 5.0.1 on 2024-04-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0013_customorder_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='customproduct',
            name='discount_price',
            field=models.IntegerField(default=0),
        ),
    ]