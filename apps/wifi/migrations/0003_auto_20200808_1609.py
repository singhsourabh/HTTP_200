# Generated by Django 2.2.14 on 2020-08-08 10:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wifi', '0002_auto_20190822_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wifidetail',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='wifidetail',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='wifidetail',
            name='new_laptop_mac_address',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, validators=[django.core.validators.RegexValidator(message='Enter MAC Address in Given Format.', regex='^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$')]),
        ),
        migrations.AlterField(
            model_name='wifidetail',
            name='old_laptop_mac_address',
            field=models.CharField(default=None, max_length=200, validators=[django.core.validators.RegexValidator(message='Enter MAC Address in Given Format.', regex='^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$')]),
        ),
        migrations.AlterField(
            model_name='wifidetail',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]