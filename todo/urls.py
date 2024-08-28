from django.urls import path
from .views import todo_create, todo_list

urlpatterns = [
   path('create/', todo_create, name='todo_create'),  # FBV
   path('', todo_list, name='todo_list'),  # FBV for listing TODO items
]