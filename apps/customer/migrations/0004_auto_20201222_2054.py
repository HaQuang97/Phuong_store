# Generated by Django 3.1.4 on 2020-12-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20201222_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.CharField(max_length=1200),
        ),
    ]
