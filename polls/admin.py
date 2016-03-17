#coding:utf-8
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question,Choice




class ChoiceInline(admin.TabularInline):
    '''
    admin.StackedInline 三个独立的list
    admin.TabularInline 样式
    '''
    model = Choice
    #3个空间
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    '''
    字段交换位置
    '''
    #fields = ['pub_date','question_text']

    #给字段写上解释语言
    fieldsets = [
        ('Good Date',{'fields':['question_text']}),
        #classes HTML样式表
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date','was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)