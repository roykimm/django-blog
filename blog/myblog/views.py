from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'myblog/index.html' # 이게 없어도 post_list로 html작업을 하면 보임

# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'myblog/index.html',
#         {'posts': posts}
#     )


class PostDetail(DetailView):
    model = Post
    #template_name = 'myblog/single_post_page.html'
# def single_post_pages(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'myblog/single_post_page.html',
#         {'post': post}
#     )
