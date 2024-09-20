from django.shortcuts import render

# Create your views here.
def introduce(request, username):
    context = {
        'name' : username
    }
    return render(request, "my_app/introduce.html", context)

def index(request):
    return render(request, "my_app/index.html")