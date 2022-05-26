from django.shortcuts import render, get_object_or_404
from .models import Group, Post


SORT_POST = 10


def index(request):
    posts = Post.objects.all()[:SORT_POST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related(
        'group').filter(group=group)[:SORT_POST]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
