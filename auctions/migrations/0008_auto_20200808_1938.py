# Generated by Django 3.0.8 on 2020-08-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200808_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Starting_Bid',
            field=models.PositiveIntegerField(),
        ),
    ]
