# Generated by Django 4.1.1 on 2022-10-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0005_alter_product_characteristics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='characteristics',
            field=models.TextField(default='{}'),
        ),
    ]
