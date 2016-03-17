#coding:utf-8
__author__ = 'similarface'

from django import template
register = template.Library()
from newblog.models import Post
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

@register.simple_tag
def total_posts():
    '''
    :return:文章的总数
    '''
    return Post.published.count()


@register.inclusion_tag('newblog/post/latest_posts.html')
def show_latest_posts(count=5):
    '''
    最新count条文章
    :param count:
    :return:最新N篇文章集合
    '''
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


# @register.filter(name='markdown')
# def markdown_format(text):
#     return mark_safe(markdown.markdown(text))




