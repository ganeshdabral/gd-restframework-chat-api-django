# Generated by Django 3.0.5 on 2020-08-27 17:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20200827_2126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatModel',
            new_name='MsgModel',
        ),
    ]