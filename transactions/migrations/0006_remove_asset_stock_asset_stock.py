# Generated by Django 4.0.3 on 2022-04-03 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_stock_remove_asset_name_remove_asset_ticker_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='stock',
        ),
        migrations.AddField(
            model_name='asset',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='transactions.stock'),
        ),
    ]
