# Generated by Django 2.2.2 on 2019-10-09 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0014_auto_20191009_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 9, 16, 17, 51, 708438)),
        ),
    ]
