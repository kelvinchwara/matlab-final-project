# Generated by Django 5.1.3 on 2024-12-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexurapp', '0011_orders_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('menu', models.CharField(max_length=100)),
                ('guests', models.IntegerField()),
                ('arrival', models.DateTimeField()),
                ('departure', models.DateTimeField()),
                ('requests', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]