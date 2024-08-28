from django.shortcuts import render, redirect
from .forms import TodoItemForm
from .models import TodoItem

def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')  # Redirect to the list view after saving
    else:
        form = TodoItemForm()
    
    return render(request, 'todo/todo_form.html', {'form': form})


def todo_list(request):
    todos = TodoItem.objects.all()  # Fetch all TODO items from the database
    return render(request, 'todo/todo_list.html', {'todos': todos})