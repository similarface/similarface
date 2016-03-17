# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedPerson',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
            },
            bases=('blog.person',),
        ),
    ]
