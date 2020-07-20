from django.shortcuts import render
from django.http import HttpResponse
from  .models import Article
from .models import About



def home(request):
    article=Article.objects.filter().order_by('date')[0:5]
    return render(request,'index.html',{'article':article})


def blog(request):
    blog_card=Article.objects.filter().order_by('number').reverse()
    return render(request,'blog.html',{'blog_card':blog_card})


def full_blog(request,slug):
    story=Article.objects.get(slug=slug)
    return render(request,'single.html',{'story':story})


def about(request):
    author=About.objects.all()
    return render(request,'about.html', {'author':author})
