from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title_index = 'Это главная страница проекта Yatube'
    context = {'title_index': title_index,
               'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title_group_list = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title_group_list': title_group_list,
        'posts': posts,
        'group': group,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
