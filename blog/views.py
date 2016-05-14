from django.shortcuts import render,get_object_or_404
from .models import Category,Post


def index(request):
    posts = Post.objects.order_by("-createdAt")
    context = {"posts": posts}
    return render(request,'blog/blog.html',context)

def post_single(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {"post":post}
    return render(request,'blog/single.html',context)

def posts_cat(request,slug):
    posts = Category.objects.get(slug=slug).post_set.all()
    context = {"posts": posts}
    return render(request,'blog/blog.html',context)
