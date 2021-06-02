from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreate(LoginRequiredMixin, CreateView):   # 로그인 했을 때만 보이게 하기 LoginRequiredMixin
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else :
            return redirect('/blog/')

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

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'myblog/post_list.html',
        {
            'post_list' : post_list,
            'tag' : tag,
            'categories': Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
        }
    )

def category_page(request, slug):

    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'myblog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()

        return context
    #template_name = 'myblog/single_post_page.html'
# def single_post_pages(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'myblog/single_post_page.html',
#         {'post': post}
#     )

