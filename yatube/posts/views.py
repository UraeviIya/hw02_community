from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Group, Post, User


def pagination(request, objects):
    paginator = Paginator(objects, settings.PAGINATOR_LIMIT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page


@login_required
def index(request):
    posts = Post.objects.all()
    page_obj = pagination(request, posts)
    context = {

        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related('group').filter(group=group)
    page_obj = pagination(request, posts)
    posts_count = posts.count()
    context = {
        'posts_count': posts_count,
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    posts_count = author.posts.count()
    page_obj = pagination(request, posts)
    context = {
        'author': author,
        'posts': posts,
        'posts_count': posts_count,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts_count = post.author.posts.count()
    title = post.text[0:30]
    context = {
        'posts': post,
        'posts_count': posts_count,
        'title': title
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', post.author.username)
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    edit = True
    form = PostForm(request.POST or None)
    if form.is_valid():
        post.save()
        return redirect('posts:post_detail', post_id)
    context = {
        'edit': edit,
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)
