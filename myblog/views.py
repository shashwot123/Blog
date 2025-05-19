from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    return render(request, "myblog/post_list.html", {"posts": posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "myblog/post_detail.html", {"post": post})