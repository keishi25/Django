# Generated by Django 3.1.4 on 2021-01-06 09:15

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, '5文字以上です！'), django.core.validators.RegexValidator('^[a-zA-Z0-9]*$', '英数字のみです！')])),
                ('age', models.IntegerField(default=0, validators=[app.models.check_age])),
            ],
        ),
    ]