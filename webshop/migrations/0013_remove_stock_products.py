# Generated by Django 4.1.1 on 2023-06-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0012_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='products',
        ),
    ]
