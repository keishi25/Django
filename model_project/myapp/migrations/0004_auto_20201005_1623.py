# Generated by Django 3.0.8 on 2020-10-05 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201005_1614'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Person',
        ),
    ]