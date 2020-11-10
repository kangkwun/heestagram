from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone


# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}

    return render(request, 'posts/detail.html', context)


def new(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'posts/new.html')    


def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    user = request.user
    body = request.POST['body']
    post = Post(user=user, body=body, created_at=timezone.now())
    post.save()
     

def edit(request,post_id):
    post = Post.objects.get(id=post_id)
    context={'post':post}
    return render(request, 'posts/edit.html',context)

def update(request,post_id):
    post = Post.objects.get(id=post_id)
    post.author = request.POST['author']
    post.body = request.POST['body']
    post.save()
    return redirect('posts:detail', post_id=post.id)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:index')
