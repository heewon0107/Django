from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm
# Create your views here.

def index(requset):
    diaries = Diary.objects.all()
    context = {
        'diaries' : diaries,
    }
    return render(requset, "diaries/index.html/", context)

def create(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save()
            return redirect("diaries:index")
    else:
        form = DiaryForm()

    context = {
        'form' : form

    }
    return render(request, "diaries/create.html", context)