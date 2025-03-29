from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Task

# Create your views here.
class TaskListView(ListView):
    model =Task
    #not required -----------------------------
    template_name="taskapp/tasks_list.html" 
    context_object_name="all_tasks"

class TaskDetailView(DetailView):
    model = Task