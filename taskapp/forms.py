from .models import Task,Comment
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content","comment_pic")
        