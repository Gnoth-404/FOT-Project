# Generated by Django 3.1.7 on 2021-11-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguoidung', '0003_thongtinnguoidung_tennguoidung'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinNhan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='roomchat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='thongtinnguoidung',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]