# Generated by Django 5.1.3 on 2024-12-03 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexurapp', '0007_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Arrival_Date_Time',
            new_name='arrival',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Departure_Date_Time',
            new_name='departure',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='E_mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Full_Name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Number_of_Guests',
            new_name='guests',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Upload_Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Room_Type',
            new_name='requests',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Special_Requests',
            new_name='room',
        ),
    ]
