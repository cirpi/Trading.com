# Generated by Django 4.0.3 on 2022-04-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]