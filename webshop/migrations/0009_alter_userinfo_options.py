# Generated by Django 4.1.1 on 2022-12-20 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0008_alter_productreview_content_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'User Info', 'verbose_name_plural': 'Users Info'},
        ),
    ]
