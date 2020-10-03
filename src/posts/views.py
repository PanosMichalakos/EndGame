from django.shortcuts import render
from .models import Post


def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.filter(review=False).order_by('-timestamp')[0:4]
    trending = Post.objects.order_by('comment_count')[0:4]
    topnews = Post.objects.filter(top_stories=True)
    latestvideo = Post.objects.filter(video=True).order_by('-timestamp')[0:1]
    latestreview = Post.objects.filter(review=True).order_by('-timestamp')[0:1]
    context = {
        'object_list': featured,
        'latest': latest,
        'topnews': topnews,
        'trending': trending,
        'latestvideo': latestvideo,
        'latestreview': latestreview
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html', {})


def post(request):
    return render(request, 'post.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def games(request):
    return render(request, 'games.html', {})
