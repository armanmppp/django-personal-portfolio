from django.shortcuts import render,get_object_or_404
from .models import Portfolio_Project
# Create your views here.
def index(request):
    projects = Portfolio_Project.objects.order_by('-id')[:4]
    context = {
        "projects":projects,
    }
    return render(request,"portfolio/index.html",context)

def allportfolio(request):
    all = Portfolio_Project.objects.order_by('-id')
    context = {
        "all":all,
    }
    return render(request,"portfolio/all_portfolio.html",context)

def detail(request,portfolio_id):
    portfolioInfo = get_object_or_404(Portfolio_Project,pk=portfolio_id)
    context = {
        "portfolioInfo":portfolioInfo,
    }
    return render(request, "portfolio/detail.html", context)