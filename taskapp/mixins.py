from .models import Task
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest

class UserIsOwnerMixin(object):
    def dispatch(self,request:HttpRequest,*args,**kwargs):
        isinstance:Task = self.get_object()
        if isinstance.user == request.user:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied