# Generated by Django 3.1.7 on 2021-12-06 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nguoidung', '0005_auto_20211206_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tinnhan',
            old_name='messenge',
            new_name='nguoigui',
        ),
    ]