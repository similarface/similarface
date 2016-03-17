# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snp', '0004_auto_20151123_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallSnp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SAMPLEID', models.CharField(max_length=24)),
                ('CHR', models.CharField(max_length=10)),
                ('STARTPOS', models.CharField(max_length=20)),
                ('ENDPOS', models.CharField(max_length=20)),
                ('REF', models.CharField(max_length=38, null=True)),
                ('ALT', models.CharField(max_length=38, null=True)),
                ('VERSION', models.IntegerField()),
                ('DEP_ACTION_TIME', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ClinVarSNP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GENE', models.CharField(max_length=32)),
                ('NUCLEOTIDE_CHANGE', models.CharField(max_length=300, null=True)),
                ('PROTEIN_CHANGE', models.CharField(max_length=300, null=True)),
                ('OTHER_MAPPINGS', models.CharField(max_length=500, null=True)),
                ('ALIAS', models.CharField(max_length=2000, null=True)),
                ('TRANSCRIPTS', models.CharField(max_length=300, null=True)),
                ('REGION', models.CharField(max_length=32, null=True)),
                ('REPORTED_CLASSIFICATION', models.CharField(max_length=300, null=True)),
                ('INFERRED_CLASSIFICATION', models.CharField(max_length=200, null=True)),
                ('SOURCE', models.CharField(max_length=80, null=True)),
                ('LAST_EVALUATED', models.CharField(max_length=12, null=True)),
                ('LAST_UPDATED', models.CharField(max_length=12, null=True)),
                ('URL', models.CharField(max_length=300, null=True)),
                ('SUBMITTER_COMMENT', models.CharField(max_length=4000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClinVarVcf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CHROM', models.CharField(max_length=24)),
                ('POS', models.CharField(max_length=20)),
                ('RSID', models.CharField(max_length=24, null=True)),
                ('REF', models.CharField(max_length=300, null=True)),
                ('ALT', models.CharField(max_length=300, null=True)),
                ('QUAL', models.CharField(max_length=300, null=True)),
                ('FILTER', models.CharField(max_length=300, null=True)),
                ('INFO', models.CharField(max_length=4000, null=True)),
                ('VERSION', models.CharField(max_length=30, null=True)),
                ('DEP_ACTION_TIME', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
