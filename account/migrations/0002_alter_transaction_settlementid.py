# Generated by Django 4.2.5 on 2024-06-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='settlementId',
            field=models.CharField(max_length=100),
        ),
    ]
