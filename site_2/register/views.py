from django.shortcuts import render,redirect,get_object_or_404

from home.models import Post
from .forms import *
from django.contrib.auth import authenticate,login as aa,logout
from django.contrib import messages
from .models import profile 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages 
# Create your views here.

def  index (request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if  form.is_valid():
          user = form.save()
          aa(request,user)
          messages.success(request,'Next step')
          return redirect('register:next_step')
        messages.error(request,'Unsuccessful registration. Invalid information.')
    form = register_form()
    return render(request,'register.html',{'form':form})    
def index_2(request):
    if request.method =='POST':
        profile_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if  profile_form.is_valid():
            profile_form.save()
            messages.success(request,'register successfully')
            return redirect('home:home')
    else:
        profile_form = profileupdateform(instance=request.user.profile)
    return render(request,'next_step.html',{'profile_form':profile_form})
    
def login (request):
    if request.method == 'POST':
        form = userlogin(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                 user = authenticate(request,username=User.objects.get(email=data['username']), password=data['password'])
            except:
                 user = authenticate(request,username=data['username'], password=data['password'])

            if user is not None:
                aa(request,user)
                messages.success(request,'your succsesfuly login')
                return redirect('home:home')
            else:
                messages.error(request,' username or passwors is incorrect')
    else:
        form=userlogin()
    return render (request,'login.html',{'form':form})


@login_required(login_url='register:login')
def userprofile(request,id):
    pro = get_object_or_404(profile,id=id)
    user_posts = Post.objects.filter(user_id= pro.user.id)
    show_followers = profile.follow
    is_follow = False
    if pro.follow.filter(id = request.user.id).exists():
        is_follow=True
    return render(request,'profile.html',{'pro':pro,'is_follow':is_follow,'show_followers':show_followers , 'user_posts':user_posts})
@login_required(login_url='register:login')
def ProfileUpdate(request):
    if request.method =='POST':
        user_form = userupdateform(request.POST,instance=request.user)
        profile_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'update successfully')
            return redirect('home:home')
    else:
        user_form = userupdateform(instance=request.user)
        profile_form = profileupdateform(instance=request.user.profile)
    return render(request,'update.html',{'user_form':user_form,'profile_form':profile_form})
@login_required(login_url='home:home')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password changes','SUCCESS')
            return redirect('register:profile')
        else:
            messages.error(request,'something went wrong, try again')
            return redirect('register:change')

    else:
        form = PasswordChangeForm(request.user)
    return  render(request,'change.html',{'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request,'loged out')
    return redirect('home:home')

def follow_user(request,id):
    follower = get_object_or_404(profile,id=id)
    is_follow = False
    if follower.follow.filter(id=request.user.id).exists():
        follower.follow.remove(request.user)
        is_follow = False
        messages.success(request,'you unfollow this user')
    else: 
        follower.follow.add(request.user)
        is_follow = True
        messages.success(request,'you follow this user')

    return redirect ('register:profile',follower.id)
