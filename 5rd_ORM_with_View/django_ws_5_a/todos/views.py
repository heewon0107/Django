from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    # work = request.GET.get('work')
    todo_list = Todo.objects.all()

    context = {
        # 'work': work
        "todo_list" : todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    # todo.work = todo
    # todo.is_completed = todo
    # todo.save()

    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)

