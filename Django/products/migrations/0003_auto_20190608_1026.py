# Generated by Django 2.2.1 on 2019-06-08 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offers',
            new_name='Offer',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
