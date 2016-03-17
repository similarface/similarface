#coding:utf-8
from django.contrib import admin

# Register your models here.
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
       list_display = ('title', 'slug', 'author', 'publish','status')
       list_filter = ('status', 'created', 'publish', 'author')
       search_fields = ('title', 'body')
       prepopulated_fields = {'slug': ('title',)}
       raw_id_fields = ('author',)
       date_hierarchy = 'publish'
       ordering = ['status', 'publish']

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
       #展示字段
       list_display = ('name', 'email', 'post', 'created', 'active')
       #过滤字段
       list_filter = ('active', 'created', 'updated')
       #搜索字段
       search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)