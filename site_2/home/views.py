from django.http import request
from home.forms import post_form
from home.models import Post
from django.shortcuts import render,redirect,get_object_or_404
from register.models import profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages as pm

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
    is_like = False
    if post.like.filter(id=requset.user.id).exists():
        is_like=True
    return render(requset,'detail.html',{'show_like':show_like,'post':post,'is_like':is_like})