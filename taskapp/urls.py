from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import RegisterView

from . import views

urlpatterns = [
  
  path('task/list/',views.TaskListView.as_view(),name = "task-list"),
  path("",views.TaskListView.as_view()),
  path('task/detail/<int:pk>',views.TaskDetailView.as_view(),name="task-detail"),
  path("task/create/",views.TaskCreateView.as_view(),name="task-create"),
  path("task/edit/<int:pk>",views.TaskEditView.as_view(),name="task-edit"),
  path("task/delete/<int:pk>", views.TaskDeleteView.as_view(),name="task-delete"),
  path('register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)