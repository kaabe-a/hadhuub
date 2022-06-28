from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm, PostForm
from . models import Category, Comment, Post
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def post_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' 
   
    object_list = Post.objects.filter(
        Q(title__contains=q) |
        Q(category__title__contains = q)
    )
    paginator = Paginator(object_list,5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context ={
        'page':page,
        'posts':posts
    }
    return render(request,'blog/post-list.html',context)

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    tags = post.tags.all()
    is_favorite = post.favorites.filter(username=request.user).exists()
    is_liked = post.likes.filter(username=request.user).exists()
    comments = post.comments.all()
    post_tag_by_id = post.tags.values_list('id',flat=True)
    similar_posts = Post.objects.filter(tags__in = post_tag_by_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                            .order_by('-same_tags','-created_at')[:4]
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None            
            if parent_id:
                parent_obj = Comment.objects.filter(id=parent_id)
                if parent_obj:
                    reply_comment = form.save(commit=False)
                    reply_comment.parent = parent_obj
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    context = {
        'post':post,
        'tags':tags,
        'categories':categories,
        'similar_posts':similar_posts,
        'is_favorite':is_favorite,
        'is_liked':is_liked,
        'comments':comments,
        'form':form,
    }
    return render(request,'blog/post-detail.html',context)

def post_category(request,category):
    posts = Post.objects.filter(category__title__icontains=category)
    context= {
        'posts':posts
    }
    return render(request,'blog/post-list.html',context)

def post_by_tag(request,tag):
    posts = Post.objects.filter(tags__name__contains = tag )
    context= {
        'posts':posts
    }
    return render(request,'blog/post-list.html',context)

@login_required(login_url='login')
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user != post.author:
        return HttpResponse('you are not allowed to edit!')
    if request.method == 'POST':
        post.delete()
        # return redirect('post-detail',po)
        
    context = {
        'post':post
    }
    return render(request,'blog/post-delete_confirm.html',context)

@login_required(login_url='login')
def post_create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.info(request,f'{post.title} has been created successfully')
            return redirect('post-detail',post.slug)
        else:    
            messages.danger(request,f'{post.title} Something Went Wrong')
    form = PostForm()
    context = {
        'form':form
    }
    return render(request,'blog/post-create.html',context)        

@login_required(login_url='login')
def post_update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user != post.author:
        return HttpResponse('you are not allowed to edit!')
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.info(request,f'{post.id} has been created successfully')
            # return redirect('post-detail',post.slug)
    form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request,'blog/post-create.html',context)  