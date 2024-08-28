from django.urls import path
from .views import todo_create

urlpatterns = [
    path('create/', todo_create, name='todo_create'),  # FBV
]