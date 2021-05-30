from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'myblog/index.html',
        {'posts': posts}
    )


def single_post_pages(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'myblog/single_post_page.html',
        {'post': post}
    )
