# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='DEP_ACTION_TIME',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='vcf',
            name='DEP_ACTION_TIME',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
