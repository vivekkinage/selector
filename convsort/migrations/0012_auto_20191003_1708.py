# Generated by Django 2.2.2 on 2019-10-03 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0011_auto_20191003_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 17, 8, 54, 555239)),
        ),
    ]