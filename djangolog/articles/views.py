from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles_list.html', { 'articles': articles })
    
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })
    # return HttpResponse(slug)

def article_detail_year(request, slug, yr):
    res = str(slug) + str(yr)
    return HttpResponse(res)

@login_required(login_url='/accounts/login/')
def article_create(request):
    return render(request, 'articles/article_create.html')