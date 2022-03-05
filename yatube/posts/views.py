from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    title_index = 'Это главная страница проекта Yatube'
    context = {'title_index': title_index}
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title_group_list = 'Здесь будет информация о группах проекта Yatube'
    context = {'title_group_list': title_group_list}
    return render(request, template, context, slug)


def group_list(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)