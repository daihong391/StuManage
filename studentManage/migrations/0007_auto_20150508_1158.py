# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentManage', '0006_auto_20150505_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminer',
            name='username',
            field=models.EmailField(default='', unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='courseName',
            field=models.CharField(default='', unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='studentId',
            field=models.CharField(default='', unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='studentName',
            field=models.CharField(default='', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='studentPassword',
            field=models.CharField(default='', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherId',
            field=models.CharField(default='', unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherName',
            field=models.CharField(default='', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherPassword',
            field=models.CharField(default='', max_length=30),
            preserve_default=True,
        ),
    ]
