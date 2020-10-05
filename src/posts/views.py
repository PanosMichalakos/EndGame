from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketing.models import Signup


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    category_count = get_category_count()
    trending = Post.objects.order_by('comment_count')[0:4]
    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'trending': trending,
        'category_count': category_count
    }
    return render(request, 'search_results.html', context)


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def index(request):
    category_count = get_category_count()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.filter(review=False).order_by('-timestamp')[0:4]
    trending = Post.objects.order_by('comment_count')[0:4]
    topnews = Post.objects.filter(top_stories=True)
    latestvideo = Post.objects.filter(video=True).order_by('-timestamp')[0:1]
    latestreview = Post.objects.filter(review=True).order_by('-timestamp')[0:1]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest': latest,
        'topnews': topnews,
        'trending': trending,
        'latestvideo': latestvideo,
        'latestreview': latestreview,
        'category_count': category_count
    }
    return render(request, 'index.html', context)


def blog(request):
    category_count = get_category_count()
    postlist = Post.objects.all()
    trending = Post.objects.order_by('comment_count')[0:4]
    paginator = Paginator(postlist, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'trending': trending,
        'category_count': category_count

    }

    return render(request, 'blog.html', context)


def post(request, id):
    return render(request, 'post.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def games(request):
    return render(request, 'games.html', {})


def reviewslist(request):
    return render(request, 'reviewslist.html')
