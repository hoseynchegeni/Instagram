from django.http import request
from .models import Post
from django.shortcuts import render,redirect,get_object_or_404
from register.models import profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages as pm
from .forms import *

@login_required(login_url='register:login')
def home(request):
    post = Post.objects.all()
    pro = profile.objects.get(user_id = request.user.id)
    form = post_form()
    show = Post.like
    return render(request,'home.html',{'pro':pro,'post':post,'form':form,'show':show})

@login_required(login_url='register:login')
def all_profile(request):
    pro = profile.objects.all()
    return render(request,'all_profile.html',{'pro':pro})

def profile_link_homepage(request,id):
    link = profile.objects.get(id=id)
    return render (request,'test.html',{'link':link})


def post(request):
    if request.method =='POST':
        form = post_form(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(text=data['text'],img=data['img'],user_id=request.user.id)
        return redirect('home:home')


def like_post(request,id):
    post = get_object_or_404(Post,id=id)
    is_like = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        is_like = False
        pm.success(request,'you disliked this post')
    else: 
        post.like.add(request.user)
        is_like = True
        pm.success(request,'you liked this post')

    return redirect ('home:detail',post.id)
    
def detail(requset,id):
    post = get_object_or_404(Post,id=id)
    show_like = post.like.all()
    comment_from = commentform()
    comment = Comment.objects.filter(poost_id=id)
    is_like = False
    if post.like.filter(id=requset.user.id).exists():
        is_like=True
    return render(requset,'detail.html',{'show_like':show_like,'post':post,'is_like':is_like,'comment_from':comment_from,'comment':comment})
def post_comment(request,id):
        post = get_object_or_404(Post,id=id)
        comment_form=commentform(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(comment=data['comment'],user_id=request.user.id,poost_id=id) 
        return redirect('home:detail',post.id)