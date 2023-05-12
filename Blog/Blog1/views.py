from django.shortcuts import render,redirect
from .models import Post
from django.views import generic

# Create your views here.
def Blogs(request):
    return render(request,"new.html")

def PostList(request):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    return render(request,"new.html",{'content':queryset})

