# Generated by Django 2.2 on 2019-11-04 18:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191104_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 18, 14, 30, 145078, tzinfo=utc)),
        ),
    ]