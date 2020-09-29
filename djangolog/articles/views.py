from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from .models import Comment
from django.contrib.auth.decorators import login_required
from .forms import CreateArticleForm
from .forms import CreateCommentForm

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles_list.html', { 'articles': articles })
    
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    form = CreateCommentForm()
    comments = Comment.objects.filter(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article, 'form': form, 'comments': comments })
    # return HttpResponse(slug)

def article_detail_year(request, slug, yr):
    res = str(slug) + str(yr)
    return HttpResponse(res)

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = CreateArticleForm()
    return render(request, 'articles/article_create.html', { 'form': form })

def article_comment(request, slug):
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = slug
            instance.save()
            return redirect('/articles/' + slug)
    # return render(request, 'articles/article_create.html', { 'form': form })
