from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import TodoItemForm
from .models import TodoItem
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


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


class TodoUpdateView(UpdateView):
    model = TodoItem
    template_name = 'todo/todo_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo:todo_list')  # Redirect to the list view after updating


@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.delete()
    return JsonResponse({'status': 'success'})