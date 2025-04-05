from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskForm
from .mixins import UserIsOwnerMixin
# Create your views here.
class TaskListView(ListView):
    model =Task
    #not required -----------------------------
    template_name="taskapp/tasks_list.html" 
    context_object_name="all_tasks"

    def get_queryset(self):
        queryset = Task.objects.filter(status="done").exclude(a=True)
        return queryset
class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin,CreateView ):
    model = Task
    form_class = TaskForm
    template_name= "taskapp/task_create.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        return super().form_valid(form)

class TaskEditView(UserIsOwnerMixin,UpdateView):
    model = Task
    form_class= TaskForm
    template_name = "taskapp/task_create.html"
    success_url = reverse_lazy("task-list")