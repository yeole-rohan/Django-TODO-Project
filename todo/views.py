from django.shortcuts import render, redirect
from .forms import TodoItemForm

def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')  # Redirect to the list view after saving
    else:
        form = TodoItemForm()
    
    return render(request, 'todo/todo_form.html', {'form': form})