from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import index, blog, post, contact, games, reviewslist, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='postlist'),
    path('post/<id>/', post, name='postdetail'),
    path('contact/', contact),
    path('games/', games),
    path('search/', search, name='search'),
    path('reviewslist/', reviewslist)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
