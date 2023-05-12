from django.urls import path
from .views import *
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("blog/",views.Blogs,name="blog"),
    path("",views.PostList,name='postList'),
]

if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)