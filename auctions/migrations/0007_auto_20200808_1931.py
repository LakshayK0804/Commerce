# Generated by Django 3.0.8 on 2020-08-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200808_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Closedlisting',
            field=models.CharField(default='The listing is open', max_length=23),
        ),
    ]
