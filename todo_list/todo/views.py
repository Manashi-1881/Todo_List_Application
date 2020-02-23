from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

# showing all the todo lists
def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'index.html', context)

# adding a new todo
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

# mark any todo as complete
def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

# delete all completed list/lists
def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

# delete all lists
def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
