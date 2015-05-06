# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentManage', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentId', models.CharField(default=b'', unique=True, max_length=30)),
                ('studentName', models.CharField(default=b'', max_length=30)),
                ('course', models.ForeignKey(to='studentManage.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
