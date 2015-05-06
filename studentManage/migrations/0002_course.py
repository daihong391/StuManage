# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseName', models.CharField(default=b'', unique=True, max_length=50)),
                ('courseCredit', models.PositiveIntegerField()),
                ('courseHour', models.PositiveIntegerField()),
                ('courseStart', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
