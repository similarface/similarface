# coding:utf-8
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from .forms import EmailPostForm
from django.shortcuts import render, get_object_or_404

from .models import PublishedManager, Post

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Comment
from .forms import CommentForm
from django.views.generic import ListView

class PostListView(ListView):
    '''
    代替下面的post_list方法
    '''
    #查询结果集
    queryset = Post.published.all()
    #填充的容器名称
    context_object_name = 'posts'
    #分页的大小
    paginate_by = 3
    #填充的模版
    template_name = 'newblog/post/list.html'


def post_list(request):
    '''
    分页代码
    :param request:
    :return:
    '''
    object_list = Post.published.all()
    #分页 3个一页
    paginator=Paginator(object_list,3)
    #获取页号
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request, 'newblog/post/list.html', {'page': page,'posts': posts})


def post_detail(request, year, month, day, post):
    #post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year)

    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #创建commetn对象但是不妨如数据库
            new_comment = comment_form.save(commit=False)
            #分配当前的post给comment
            new_comment.post = post
            #保存到数据库
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request,'newblog/post/detail.html',{'post': post,'comments': comments, 'comment_form': comment_form})



    return render(request,'newblog/post/detail.html',{'post': post})

def post_share(request,post_id):
    post=get_object_or_404(Post,id=post_id,status='Published')
    sent=False
    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form=EmailPostForm()
    return render(request,'newblog/post/share.html',{'post':post,'form':form})






