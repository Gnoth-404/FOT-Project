# Generated by Django 3.2.8 on 2021-11-11 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nguoidung', '0002_rename_user_thongtinnguoidung'),
    ]

    operations = [
        migrations.AddField(
            model_name='thongtinnguoidung',
            name='tennguoidung',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
