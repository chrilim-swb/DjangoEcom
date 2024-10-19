# Generated by Django 5.1.1 on 2024-10-06 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_address2_shippingaddress_shoping_address1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_address1',
            new_name='shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_address2',
            new_name='shipping_address2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_city',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_country',
            new_name='shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_email',
            new_name='shipping_email',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_full_name',
            new_name='shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_state',
            new_name='shipping_state',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shoping_zipcode',
            new_name='shipping_zipcode',
        ),
    ]
