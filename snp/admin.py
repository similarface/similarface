from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import CSV,VCF

class CSVAdmin(admin.ModelAdmin):
    list_display = ('SAMPLEID', 'CHR','STARTPOS','SNP138')

class VCFAdmin(admin.ModelAdmin):
    list_display = ('SAMPLEID', 'CHROM','POS','RSID')

admin.site.register(CSV,CSVAdmin)
admin.site.register(VCF,VCFAdmin)