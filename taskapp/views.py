from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task,Comment
from .forms import CommentForm, TaskForm
from .mixins import UserIsOwnerMixin

# Create your views here.
class TaskListView(ListView):
    model =Task
    #not required -----------------------------
    template_name="taskapp/tasks_list.html" 
    context_object_name="all_tasks"

    # def get_queryset(self):
    #     queryset = Task.objects.filter(status="done").exclude(priority=True)
    #     return queryset
class TaskDetailView(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]= CommentForm()
        return context

    def post(self,request :HttpRequest,*args,**kwargs):
        if request.user.is_authenticated:
            print("_-----------------------")
            print(request.FILES)
            print("_-----------------------")
            form = CommentForm(request.POST,request.FILES)

            if form.is_valid():
                new_comment: Comment = form.instance
                new_comment.task = self.get_object()
                new_comment.user = self.request.user
                new_comment.save()
            return redirect(request.path_info)
        else:
            return HttpRequest(content="Must be authenticated",status=403)
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
    #success_url = reverse_lazy("task-list")
    def get_success_url(self):
        url = reverse("task-detail",kwargs={"pk": self.get_object().pk})
        return url

class TaskDeleteView(UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = "taskapp/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")