from django.shortcuts import render,get_object_or_404
from .models import Blogs
# Create your views here.

def index(request):
    allblog = Blogs.objects.all()
    context = {
        "allblog":allblog,
    }
    return render(request,"blog/all_blogs.html",context)

def detail(request,blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id)
    context = {
        "blog": blog,
    }
    return render(request, "blog/detail.html", context)