from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Myron',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date': 'August 27, 2018',
    },
    {
        'author': 'Myron',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date': 'August 27, 2018',
    },
    {
        'author': 'Myron',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date': 'August 27, 2018',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "DING DONG"})
