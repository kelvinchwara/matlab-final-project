# Generated by Django 5.1.3 on 2024-12-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexurapp', '0006_imagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=100)),
                ('E_mail', models.EmailField(max_length=100)),
                ('Room_Type', models.CharField(max_length=100)),
                ('Number_of_Guests', models.IntegerField()),
                ('Arrival_Date_Time', models.DateField()),
                ('Departure_Date_Time', models.DateField()),
                ('Special_Requests', models.CharField(max_length=100)),
                ('Upload_Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
