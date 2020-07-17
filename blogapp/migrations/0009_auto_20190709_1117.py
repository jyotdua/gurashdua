# Generated by Django 2.2.2 on 2019-07-09 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20190709_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='owner',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 5, 47, 49, 848505, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 5, 47, 49, 847965, tzinfo=utc)),
        ),
    ]
