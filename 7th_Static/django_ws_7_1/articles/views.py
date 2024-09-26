from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'articles' : article,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    
    if request.method == "POST":
        # articles = Article(request.POST)
        # articles.save()
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)