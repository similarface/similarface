# coding:utf-8
__author__ = 'similarface'
from django import forms

class EmailPostForm(forms.Form):
    '''
    email的form标签体
    '''
    #
    name = forms.CharField(max_length=25)
    #发件人
    email=forms.EmailField()
    #收件人
    to=forms.EmailField()
    #消息内容
    comments=forms.CharField(required=False,widget=forms.Textarea)



from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name', 'email', 'body')

