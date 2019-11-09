# Generated by Django 2.2.2 on 2019-10-03 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0009_auto_20191003_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvs',
            name='path',
            field=models.CharField(default='resume.html', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvs',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 16, 50, 30, 715183)),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 16, 50, 30, 714702)),
        ),
    ]