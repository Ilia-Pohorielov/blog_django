from django.shortcuts import render, get_object_or_404
# from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blogs/homepage.html',
        {'posts': posts}
    )

def post_new(request):
    form = PostForm()
    return render(
        request,
        'blogs/blog_add.html',
        {'form': form}
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        'blogs/inner_blog.html',
        {'post': post}
    )
