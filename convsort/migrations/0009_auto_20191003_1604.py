# Generated by Django 2.2.2 on 2019-10-03 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convsort', '0008_auto_20191003_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='REGISTRATIONS',
            fields=[
                ('user_key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(default='something', max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='cvs',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 16, 4, 27, 808458)),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 16, 4, 27, 808226)),
        ),
    ]