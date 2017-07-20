from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.core.exceptions import ValidationError
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
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('post_detail', pk=post.pk )

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
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
        form = PostForm(request.POST, request.FILES, instance=post)
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
def post_delete(request,pk):
    Post.objects.get(pk=pk).delete()
    return redirect('post_list')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_r = request.POST.get('password_r')
        user = User(username=username)
        User(email=email)
        if password == password_r:
            user.set_password(password)
        user.save()
        return redirect('login')
    return render(
        request,
        'blogs/register_page.html',
    )

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login_user(request, user)
        return redirect('post_list')
    return render(
        request,
        'blogs/login_page.html'
    )

def logout(request):
    logout_user(request)
    return redirect('post_list')