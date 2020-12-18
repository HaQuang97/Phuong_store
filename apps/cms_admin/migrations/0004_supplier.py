# Generated by Django 3.1.4 on 2020-12-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_admin', '0003_auto_20201218_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
    ]