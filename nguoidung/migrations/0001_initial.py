# Generated by Django 3.2.8 on 2021-11-10 06:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomID', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
                ('nation', django_countries.fields.CountryField(max_length=2)),
                ('dateofbirth', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ'), ('O', 'Khác')], default='', max_length=1)),
                ('room', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='nguoidung.roomchat')),
            ],
        ),
    ]
