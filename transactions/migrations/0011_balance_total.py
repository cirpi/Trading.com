# Generated by Django 4.0.3 on 2022-04-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='total',
            field=models.FloatField(default=10000),
        ),
    ]
