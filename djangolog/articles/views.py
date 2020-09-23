from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles_list.html', { 'articles': articles })
    
def article_detail(request, slug):
    return HttpResponse(slug)

def article_detail_year(request, slug, yr):
    res = str(slug) + str(yr)
    return HttpResponse(res)