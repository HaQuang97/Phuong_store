# Generated by Django 3.1.4 on 2021-01-04 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_admin', '0004_auto_20210104_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Cash'), (2, 'Credit Card')], default=1),
        ),
    ]
