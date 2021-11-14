from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo

def Todo_list(request):
    todos = Todo.objects.all()
    context ={
        "todo_list": todos
    }
    return render(request, "Todo/todo_list.html", context)


def Todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "Todo/todo_detail.html", context)



def Todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = { "form":form}
    return render(request, "Todo/todo_create.html", context) 


def Todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = { "form":form}
    return render(request, "Todo/todo_update.html", context) 

def Todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")
