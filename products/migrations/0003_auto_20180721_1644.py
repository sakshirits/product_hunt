# Generated by Django 2.0.5 on 2018-07-21 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180721_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='icons',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]
