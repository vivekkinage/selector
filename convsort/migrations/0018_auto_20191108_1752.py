# Generated by Django 2.2.2 on 2019-11-08 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0017_auto_20191108_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvs',
            name='job',
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 8, 17, 52, 21, 150848)),
        ),
    ]