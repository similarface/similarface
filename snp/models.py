#coding:utf-8
from django.db import models
import datetime
# Create your models here.

class VCF(models.Model):
    '''
    pipeline 生成的vcf文件
    '''
    SAMPLEID=models.CharField(max_length=36,null=False)
    CHROM=models.CharField(max_length=12,null=False)
    POS=models.CharField(max_length=20,null=False)
    RSID=models.CharField(max_length=18,null=True)
    REF=models.CharField(max_length=16,null=True)
    ALT=models.CharField(max_length=16,null=True)
    QUAL=models.DecimalField(max_digits=10, decimal_places=3,null=True)
    FILTER=models.CharField(max_length=20,null=True)
    FORMAT=models.CharField(max_length=30,null=True)
    EXAMDATA=models.CharField(max_length=50,null=True)
    SORTQUE=models.CharField(max_length=5,null=True)
    GENTYPE=models.CharField(max_length=5,null=True)
    INFO=models.CharField(max_length=2000,null=True)
    DEP_ACTION_TIME=models.DateTimeField(null=False,default=datetime.datetime.now)

    def __str__(self):
        return self.SAMPLEID+"_"+self.CHROM+"_"+self.POS+"_"+self.RSID

class CSV(models.Model):
    '''
    pipeline 生成的csv文件
    '''
    SAMPLEID=models.CharField(max_length=24,null=False)
    CHR=models.CharField(max_length=10,null=False)
    STARTPOS=models.CharField(max_length=20,null=False)
    ENDPOS=models.CharField(max_length=20,null=False)
    REF=models.CharField(max_length=38,null=True)
    ALT=models.CharField(max_length=38,null=True)
    FUNC_REFGENE=models.CharField(max_length=32,null=True)
    GENE_REFGENE=models.CharField(max_length=28,null=True)
    GENEDETAIL_REFGENE=models.CharField(max_length=1000,null=True)
    EXONICFUNC_REFGENE=models.CharField(max_length=88,null=True)
    AACHANGE_REFGENE=models.CharField(max_length=1000,null=True)
    CYTOBAND=models.CharField(max_length=80,null=True)
    GENOMICSUPERDUPS=models.CharField(max_length=80,null=True)
    ESP6500SIV2_ALL=models.CharField(max_length=80,null=True)
    C_1000G2014OCT_ALL=models.CharField(max_length=80,null=True)
    C_1000G2014OCT_AFR=models.CharField(max_length=80,null=True)
    C_1000G2014OCT_EAS=models.CharField(max_length=80,null=True)
    C_1000G2014OCT_EUR=models.CharField(max_length=80,null=True)
    SNP138=models.CharField(max_length=80,null=True)
    SIFT_SCORE=models.CharField(max_length=64,null=True)
    SIFT_PRED=models.CharField(max_length=64,null=True)
    POLYPHEN2_HDIV_SCORE=models.CharField(max_length=64,null=True)
    POLYPHEN2_HDIV_PRED=models.CharField(max_length=24,null=True)
    POLYPHEN2_HVAR_SCORE=models.CharField(max_length=24,null=True)
    POLYPHEN2_HVAR_PRED=models.CharField(max_length=26,null=True)
    LRT_SCORE=models.CharField(max_length=16,null=True)
    LRT_PRED=models.CharField(max_length=24,null=True)
    MUTATIONTASTER_SCORE=models.CharField(max_length=10,null=True)
    MUTATIONTASTER_PRED=models.CharField(max_length=18,null=True)
    MUTATIONASSESSOR_SCORE=models.CharField(max_length=10,null=True)
    MUTATIONASSESSOR_PRED=models.CharField(max_length=10,null=True)
    FATHMM_SCORE=models.CharField(max_length=10,null=True)
    FATHMM_PRED=models.CharField(max_length=10,null=True)
    RADIALSVM_SCORE=models.CharField(max_length=10,null=True)
    RADIALSVM_PRED=models.CharField(max_length=10,null=True)
    LR_SCORE=models.CharField(max_length=10,null=True)
    LR_PRED=models.CharField(max_length=10,null=True)
    VEST3_SCORE=models.CharField(max_length=10,null=True)
    CADD_RAW=models.CharField(max_length=10,null=True)
    CADD_PHRED=models.CharField(max_length=10,null=True)
    GERP_RS=models.CharField(max_length=10,null=True)
    PHYLOP46WAY_PLACENTAL=models.CharField(max_length=10,null=True)
    PHYLOP100WAY_VERTEBRATE=models.CharField(max_length=10,null=True)
    SIPHY_29WAY_LOGODDS=models.CharField(max_length=10,null=True)
    DEP_ACTION_TIME=models.DateTimeField(null=False,default=datetime.datetime.now)


    def __str__(self):
        return self.SAMPLEID+"_"+self.CHR+"_"+self.STARTPOS+"_"+self.SNP138


class CallSnp(models.Model):
    '''
    call 出来的变异
    '''
    SAMPLEID=models.CharField(max_length=24,null=False)
    CHR=models.CharField(max_length=10,null=False)
    STARTPOS=models.CharField(max_length=20,null=False)
    ENDPOS=models.CharField(max_length=20,null=False)
    REF=models.CharField(max_length=38,null=True)
    ALT=models.CharField(max_length=38,null=True)
    VERSION=models.IntegerField()
    DEP_ACTION_TIME=models.DateTimeField(null=False,default=datetime.datetime.now)


class ClinVarVcf(models.Model):
    CHROM=models.CharField(max_length=24)
    POS=models.CharField(max_length=20,null=False)
    RSID=models.CharField(max_length=24,null=True)
    REF=models.CharField(max_length=300,null=True)
    ALT=models.CharField(max_length=300,null=True)
    QUAL=models.CharField(max_length=300,null=True)
    FILTER=models.CharField(max_length=300,null=True)
    INFO=models.CharField(max_length=4000,null=True)
    VERSION=models.CharField(max_length=30,null=True)
    DEP_ACTION_TIME=models.DateTimeField(null=False,default=datetime.datetime.now)

class ClinVarSNP(models.Model):
    GENE=models.CharField(max_length=32,null=False)
    NUCLEOTIDE_CHANGE=models.CharField(max_length=300,null=True)
    PROTEIN_CHANGE=models.CharField(max_length=300,null=True)
    OTHER_MAPPINGS=models.CharField(max_length=500,null=True)
    ALIAS=models.CharField(max_length=2000,null=True)
    TRANSCRIPTS=models.CharField(max_length=300,null=True)
    REGION=models.CharField(max_length=32,null=True)
    REPORTED_CLASSIFICATION=models.CharField(max_length=300,null=True)
    INFERRED_CLASSIFICATION=models.CharField(max_length=200,null=True)
    SOURCE=models.CharField(max_length=80,null=True)
    LAST_EVALUATED=models.CharField(max_length=12,null=True)
    LAST_UPDATED=models.CharField(max_length=12,null=True)
    URL=models.CharField(max_length=300,null=True)
    SUBMITTER_COMMENT=models.CharField(max_length=4000,null=True)