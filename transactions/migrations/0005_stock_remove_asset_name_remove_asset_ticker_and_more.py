# Generated by Django 4.0.3 on 2022-04-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_asset_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='name',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='ticker',
        ),
        migrations.AddField(
            model_name='asset',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Price per stock'),
        ),
        migrations.AddField(
            model_name='asset',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='stock',
            field=models.ManyToManyField(related_name='stock', to='transactions.stock'),
        ),
    ]