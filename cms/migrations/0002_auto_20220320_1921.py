# Generated by Django 3.2.8 on 2022-03-20 13:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='CMSMenu',
        ),
        migrations.RenameModel(
            old_name='MenuItem',
            new_name='CMSMenuContent',
        ),
    ]