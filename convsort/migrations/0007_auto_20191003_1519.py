# Generated by Django 2.2.2 on 2019-10-03 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0006_auto_20191003_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvs',
            name='uid',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvs',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 15, 19, 27, 496750)),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 15, 19, 27, 496495)),
        ),
    ]
