# Generated by Django 3.1.4 on 2020-12-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_admin', '0002_auto_20201228_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Success'), (2, 'Failure')], default=1),
        ),
    ]
