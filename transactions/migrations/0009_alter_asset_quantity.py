# Generated by Django 4.0.3 on 2022-04-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_alter_asset_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='quantity',
            field=models.FloatField(),
        ),
    ]