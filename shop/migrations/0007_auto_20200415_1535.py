# Generated by Django 3.0.5 on 2020-04-15 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_orders_address2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='address1',
            new_name='address',
        ),
    ]
