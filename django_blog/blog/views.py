from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Category, Post

# def index(request):
#     title = 'Blogosphere'
#     posts = Post.objects.exclude(pub_date__gt=timezone.now()).order_by('-pub_date')
#     context = {
#         'title': title,
#         'posts': posts,
#     }
#     return render(request, "blog/index.html", context)

class IndexView( ListView):
    template_name = "blog/index.html"
    extra_context = {
        'title': 'Blogosphere',
    }
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.exclude(pub_date__gt=timezone.now()).order_by('-pub_date')


def details(request, post_id):
    # szczegóły wpisu dla zalgowantych
    post = Post.objects.get(id=post_id)
    title = post.post_title
    context = {
        'title': title,
        'post': post,
    }
    return render(request, "blog/details.html", context)


# Przeglądanie własnych wpisów (dla zalogowanych)
# Tworzenie własnych wpisów (dla zalogowanych)
# Edycja własnych wpisów (dla zalogowanych)