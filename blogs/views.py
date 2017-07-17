from django.shortcuts import render, get_object_or_404
# from django.utils import timezone
from .models import Post
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
    return render(
        request,
        'blogs/inner_blog.html',
        {'post': post}
    )
