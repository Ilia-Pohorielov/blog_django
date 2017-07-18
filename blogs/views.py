from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blogs/homepage.html',
        {'posts': posts}
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(
        request,
        'blogs/inner_blog.html',
        {
            'post': post,
            'form': comment_form,
            'comments': post.comments.all(),
        }
    )

def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.instance
        comment.post = post
        comment.save()
    return redirect('post_detail', pk=post.pk )

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(
        request,
        'blogs/blog_add.html',
        {'form': form}
    )

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(
        request,
        'blogs/blog_edit.html',
        {'form': form}
    )

