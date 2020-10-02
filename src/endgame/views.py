from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def post(request):
    return render(request, 'post.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def games(request):
    return render(request, 'games.html', {})
