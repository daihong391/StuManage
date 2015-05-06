# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentManage', '0005_course_coursepeople'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentPassword',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacherPassword',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
    ]
