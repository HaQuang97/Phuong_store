# Generated by Django 3.1.4 on 2020-12-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('number_credit', models.CharField(max_length=20)),
                ('expire_date', models.DateField()),
                ('CVV', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'credit_card',
            },
        ),
    ]
