from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title= models.CharField(max_length=50, verbose_name='task`s title')
    description = models.TextField(verbose_name='description of the task')
    
    STATUS_CHOICES = [
            ("in_prog", "In Progress"),
            ("done", "Done"),
            ("delayed", "Delayed"),
            ("not_start", "Not Started"),

    ]
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default="not_start")

    PRIORITY_CHOICES = {
        "low": "Low Priority",
        "mid": "Medium Priority",
        "high": "High Priority",
    }

    priority = models.CharField(max_length=5,choices=PRIORITY_CHOICES,default="mid")

    due_to=models.DateTimeField(null=True,blank=True)

    user= models.ForeignKey(User, on_delete=models.CASCADE)