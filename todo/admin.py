from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
