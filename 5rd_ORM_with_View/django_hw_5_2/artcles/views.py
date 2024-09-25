from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        "articles" : articles,

    }
    return render(request, "articles/index.html", context)

def new(request):
    return render(request, "articles/new.html")

def create(request):
    
    article = Article()
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    # created_at = request.POST.get("created_at")
    # = request.POST.get("")
    article.save()
    return redirect("articles:index")
