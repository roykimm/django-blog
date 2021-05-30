from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()

        return context

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
