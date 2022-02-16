from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('admin/', admin.site.urls)
    #path('posts/<slug:groups>/', views.group_posts())
    path(
        'group/<slug:slug>/',
        views.group_posts
    ),
]