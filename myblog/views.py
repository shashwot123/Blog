from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import Post, Comments
from .forms import CommentForm, CustomUserCreationForm

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    return render(request, "myblog/post_list.html", {"posts": posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comments.objects.filter(post=post).order_by("-created_at")

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            #don't save because we don't know which post the comment is for
            comment = form.save(commit=False)
            #save to the related post
            comment.post = post
            comment.save()
    else:
        #not a POST request
        form = CommentForm()
    
    return render(request, "myblog/post_detail.html", {
        "post": post,
        "comments" : comments,
        "form": form})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html",{"form": form})