from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from .models import Comment
from django.contrib.auth.decorators import login_required
from .forms import CreateArticleForm
from .forms import CreateCommentForm
from .forms import EditArticleForm

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

def article_edit(request, slug):
    # print('Reached POST request=============================================================')
    if request.method == 'POST':
        article = Article.objects.get(slug=slug)
        print(request.POST)
        print(request.FILES)
        article.title = request.POST['title']
        article.body = request.POST['body']
        article.thumb = request.FILES['thumb']
        article.save()
        return redirect('/articles/' + slug)
    else:
        article = Article.objects.get(slug=slug)
        # Make form with filled values of the article
        print(article.thumb)
        form = EditArticleForm()
        form.setValues(article.title, article.body, article.thumb)
        return render(request, 'articles/article_edit.html', { 'form': form, 'old_slug': slug })