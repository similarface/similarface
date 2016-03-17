# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SAMPLEID', models.CharField(max_length=24)),
                ('CHR', models.CharField(max_length=10)),
                ('STARTPOS', models.CharField(max_length=20)),
                ('ENDPOS', models.CharField(max_length=20)),
                ('REF', models.CharField(max_length=38, null=True)),
                ('ALT', models.CharField(max_length=38, null=True)),
                ('FUNC_REFGENE', models.CharField(max_length=32, null=True)),
                ('GENE_REFGENE', models.CharField(max_length=28, null=True)),
                ('GENEDETAIL_REFGENE', models.CharField(max_length=1000, null=True)),
                ('EXONICFUNC_REFGENE', models.CharField(max_length=88, null=True)),
                ('AACHANGE_REFGENE', models.CharField(max_length=1000, null=True)),
                ('CYTOBAND', models.CharField(max_length=80, null=True)),
                ('GENOMICSUPERDUPS', models.CharField(max_length=80, null=True)),
                ('ESP6500SIV2_ALL', models.CharField(max_length=80, null=True)),
                ('C_1000G2014OCT_ALL', models.CharField(max_length=80, null=True)),
                ('C_1000G2014OCT_AFR', models.CharField(max_length=80, null=True)),
                ('C_1000G2014OCT_EAS', models.CharField(max_length=80, null=True)),
                ('C_1000G2014OCT_EUR', models.CharField(max_length=80, null=True)),
                ('SNP138', models.CharField(max_length=80, null=True)),
                ('SIFT_SCORE', models.CharField(max_length=64, null=True)),
                ('SIFT_PRED', models.CharField(max_length=64, null=True)),
                ('POLYPHEN2_HDIV_SCORE', models.CharField(max_length=64, null=True)),
                ('POLYPHEN2_HDIV_PRED', models.CharField(max_length=24, null=True)),
                ('POLYPHEN2_HVAR_SCORE', models.CharField(max_length=24, null=True)),
                ('POLYPHEN2_HVAR_PRED', models.CharField(max_length=26, null=True)),
                ('LRT_SCORE', models.CharField(max_length=16, null=True)),
                ('LRT_PRED', models.CharField(max_length=24, null=True)),
                ('MUTATIONTASTER_SCORE', models.CharField(max_length=10, null=True)),
                ('MUTATIONTASTER_PRED', models.CharField(max_length=18, null=True)),
                ('MUTATIONASSESSOR_SCORE', models.CharField(max_length=10, null=True)),
                ('MUTATIONASSESSOR_PRED', models.CharField(max_length=10, null=True)),
                ('FATHMM_SCORE', models.CharField(max_length=10, null=True)),
                ('FATHMM_PRED', models.CharField(max_length=10, null=True)),
                ('RADIALSVM_SCORE', models.CharField(max_length=10, null=True)),
                ('RADIALSVM_PRED', models.CharField(max_length=10, null=True)),
                ('LR_SCORE', models.CharField(max_length=10, null=True)),
                ('LR_PRED', models.CharField(max_length=10, null=True)),
                ('VEST3_SCORE', models.CharField(max_length=10, null=True)),
                ('CADD_RAW', models.CharField(max_length=10, null=True)),
                ('CADD_PHRED', models.CharField(max_length=10, null=True)),
                ('GERP_RS', models.CharField(max_length=10, null=True)),
                ('PHYLOP46WAY_PLACENTAL', models.CharField(max_length=10, null=True)),
                ('PHYLOP100WAY_VERTEBRATE', models.CharField(max_length=10, null=True)),
                ('SIPHY_29WAY_LOGODDS', models.CharField(max_length=10, null=True)),
                ('DEP_ACTION_TIME', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VCF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SAMPLEID', models.CharField(max_length=36)),
                ('CHROM', models.CharField(max_length=12)),
                ('POS', models.CharField(max_length=20)),
                ('RSID', models.CharField(max_length=18, null=True)),
                ('REF', models.CharField(max_length=16, null=True)),
                ('ALT', models.CharField(max_length=16, null=True)),
                ('QUAL', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('FILTER', models.CharField(max_length=20, null=True)),
                ('FORMAT', models.CharField(max_length=30, null=True)),
                ('EXAMDATA', models.CharField(max_length=50, null=True)),
                ('SORTQUE', models.CharField(max_length=5, null=True)),
                ('GENTYPE', models.CharField(max_length=5, null=True)),
                ('INFO', models.CharField(max_length=2000, null=True)),
                ('DEP_ACTION_TIME', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
