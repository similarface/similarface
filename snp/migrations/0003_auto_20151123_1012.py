# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snp', '0002_auto_20151123_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='DEP_ACTION_TIME',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vcf',
            name='DEP_ACTION_TIME',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
