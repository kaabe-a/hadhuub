from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from . decorators import unauthenticated_user
from django.db.models import F

from blog.models import Post
from . models import Follow, User
from . import forms

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'you have logged successfully')
                return redirect('profile',request.user.username)
            else:
                messages.error(request,'Something went wrong body')
    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

# @login_required(login_url='login')
@unauthenticated_user
def register_page(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # print(user.groups.all())
            username = form.cleaned_data.get('username')
            messages.success(request,'Account Was Created For'+username)
            return redirect('login')
    form = forms.UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/register.html',context)

def profile(request,username):
    user = get_object_or_404(User,username=username,is_active=True)
    # all the posts of the user
    # user profile bio, first name link to contact with
    posts = user.post_set.all()
    total_posts = user.post_set.filter(status='P').count()
    context = {
        "user":user,
        'posts':posts,
        'total_posts':total_posts
    }
    return render(request,'accounts/profile.html',context)

@login_required(login_url='login')
def publish_or_unpublish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if post.author == request.user:
        if post.status == 'P':
            post.status = 'D'
            post.save()
            print(post.status)
        else:
            post.status = 'P'
            post.save()
            print(post.status)
    return redirect('profile',request.user)
    

@login_required(login_url='login')
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        uform = forms.UserEditForm(request.POST,instance=user)
        pform = forms.ProfileForm(request.POST,request.FILES,instance=user.profile)
        sform = forms.SocialForm(request.POST,instance=user.social)
        if uform.is_valid() and pform.is_valid() and sform.is_valid():
            uform.save()
            pform.save()
            social = sform.save(commit=False)
            social.user = user
            social.save()
            messages.success(request,'Profile have been updated successfuly')
        else:
            messages.error(request,'Sorry some thing went wrong Please try again')
    uform = forms.UserEditForm(instance=user)
    pform = forms.ProfileForm(instance=user.profile)
    sform = forms.SocialForm(instance=user.social)
    context = {
        'pform':pform,
        'uform':uform,
        'sform':sform,
    }
    return render(request,'accounts/profile_update.html',context)

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def users_page(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'accounts/users.html',context)  


@login_required(login_url='login')
def add_favorite(request,pk):
    post = get_object_or_404(Post,pk=pk)
    user = request.user
    print(user,post.favorites.all())
    if not post.favorites.filter(username=user).exists():
        post.favorites.add(user)
    else:
        post.favorites.remove(user)
    return redirect('fav')
    
@login_required(login_url='login')
def my_favorite(request):
    favorites = request.user.favorites.filter(status='P').all()
    total_posts = request.user.post_set.filter(status='P').count()
    # total_posts = user.post_set.filter(status='P').count()
    context = {
        'favorites':favorites,
        'total_posts':total_posts
    }
    return render(request,'accounts/fav.html',context)


@login_required(login_url='login')
def like_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    user = request.user
    if not post.likes.filter(username=user).exists():
        post.likes.add(user)
        post.like_count = post.likes.all().count()
        post.save()
    else:
        post.likes.remove(user)
        post.like_count = post.likes.all().count()
        post.save()        
    return redirect('post-detail',post.slug)




#Do Follow Or UnFollow
@login_required(login_url='login')
def follow(request,pk):
    current_user = request.user
    print(current_user,'is following')
    user_to_follow = User.objects.get(pk=pk)
    print(user_to_follow,'to follow')
    if not Follow.objects.filter(user_is_following=current_user,\
        user_to_follow=user_to_follow).exists() and user_to_follow != request.user:
        (follow,created) = Follow.objects.get_or_create(user_is_following=current_user,\
            user_to_follow=user_to_follow)
        print(follow)
    else:
        Follow.objects.filter(user_is_following=current_user,user_to_follow=user_to_follow).delete()
        print('boodaysay')
    return redirect('profile',current_user)
        