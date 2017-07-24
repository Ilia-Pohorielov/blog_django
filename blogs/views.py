from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.core.exceptions import ValidationError
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='publish')
    return render(
        request,
        'blogs/homepage.html',
        {'posts': posts}
    )
def user_page(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user)
    return render(
        request,
        'blogs/user_page.html',
        {
            'posts': posts,
            'user': user
        }
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

def admin_account(request):
    posts = Post.objects.filter(status='expectation')
    return render(
        request,
        'blogs/admin_account.html',
        {
            'posts': posts,
        }
    )

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
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
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login_user(request, new_user)
            return redirect('post_list')
    return render(
        request,
        'blogs/register_page.html',
        {'form': form}
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