# Generated by Django 4.0.2 on 2022-03-22 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_alter_log_date_alter_log_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 3, 53, 55, 956840)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2022, 3, 22, 3, 53, 55, 956840)),
        ),
    ]
