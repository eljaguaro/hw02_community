from django.shortcuts import render, get_object_or_404
from .models import Post, Group

last_ten = 10


# Главная страница
def index(request):
    posts = Post.objects.all()[:last_ten]
    context = {
        'posts': posts,
    }
    template = 'posts/index.html'
    return render(request, template, context)


# Страница со сгруппированными постами
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:last_ten]
    context = {
        'group': group,
        'posts': posts
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
