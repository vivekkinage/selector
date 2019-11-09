# Generated by Django 2.2.2 on 2019-10-03 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0005_auto_20191003_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvs',
            name='path',
        ),
        migrations.AddField(
            model_name='cvs',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='cvs',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 14, 46, 39, 933630)),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 14, 46, 39, 933242)),
        ),
    ]