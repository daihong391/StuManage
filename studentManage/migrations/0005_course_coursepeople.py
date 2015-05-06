# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentManage', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coursePeople',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
