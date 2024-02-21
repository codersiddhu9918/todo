from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo

def todo_list(request):
    x = {'item': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', x)
def insert_todo_items(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('main')
def delete_todo_items(request,todo_id):
    todoid = Todo.objects.get(id=todo_id)
    todoid.delete()
    return redirect('main')


# Create your views here.
