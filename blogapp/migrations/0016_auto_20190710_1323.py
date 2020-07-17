# Generated by Django 2.2.2 on 2019-07-10 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20190709_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='country_name',
            field=django_countries.fields.CountryField(default='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 7, 53, 19, 126001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 7, 53, 19, 125001, tzinfo=utc)),
        ),
    ]
