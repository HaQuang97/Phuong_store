# Generated by Django 3.1.4 on 2020-12-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_admin', '0003_orders_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='payment_type',
        ),
    ]
