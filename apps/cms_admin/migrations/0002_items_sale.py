# Generated by Django 3.1.4 on 2020-12-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='sale',
            field=models.IntegerField(default=None),
        ),
    ]