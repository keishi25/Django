# Generated by Django 3.0.8 on 2020-10-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=100, null=True)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('sex', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
