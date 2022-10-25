from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Group, Post, User

POST_PER_PAGE = 10

def index(request):
    post_list = (
        Post.objects.all()
    )
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (
        Post.objects.filter(group=group)[:POST_PER_PAGE]
    )

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    page_obj = author.posts.all()
    context = {
        'page_obj': page_obj,
        'author': author,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'posts/post_detail.html', context)


def create_post(request):
    context = {

    }
    return render(request, 'posts/create_post.html', context)