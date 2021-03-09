from django.shortcuts import render
from django.utils import timezone

from .models import Category, Post

def index(request):
    title = 'Blogosphere'
    posts = Post.objects.exclude(pub_date__gt=timezone.now()).order_by('-pub_date')
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, "blog/index.html", context)

# class IndexView(PostsNotInFutureMixin, ListView):
#     template_name = "blog/index.html"
#     extra_context = {
#         'title': 'Blogosphere',
#     }
#     context_object_name = "posts"


def details(request, post_id):
    # szczegóły wpisu dla zalgowantych
    post = Post.objects.get(id=post_id)
    title = post.title
    context = {
        'title': title,
        'post': 'post'
    }
    return render(request, "blog/details.html", context)
