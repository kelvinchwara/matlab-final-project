# Generated by Django 5.1.3 on 2024-12-04 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexurapp', '0017_ordersmodel_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrdersModel',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='image',
        ),
    ]
