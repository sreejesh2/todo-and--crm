from django.shortcuts import render,redirect
from .models import Todos
from .forms import TodosForm,RegistrationForm
from  django.views.generic import View,FormView
from django.contrib.auth.models import User

# Create your views here.
class TodoCreateView(View):
    def get(self,request,*args, **kwargs):
        form=TodosForm()
        return render(request,"todo-create.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=TodosForm(request.POST)
        if form.is_valid():
           Todos.objects.create(**form.cleaned_data)
           return redirect('all-todo')
        
        return render(request,'todo-create.html',{"form":form})
    
class TodoListView(View):
    def get(self,request,*args, **kwargs):
            
        qs=Todos.objects.all().order_by("-date")
        return render(request,'todo-list.html',{"todos":qs})

class TodoDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get('pk')
        qs=Todos.objects.get(id=id)
        context={"todo":qs}
        return render(request,'todo-detail.html',context)
    
class TodoDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk") 
        Todos.objects.get(id=id).delete()  
        return redirect("all-todo") 
    
# class TodoUpdateView(View):
#     def get(self,request,*args, **kwargs):
            
#             form=TodosForm()
#             return render(request,'edit.html',{"form":form})
#     def post(self,request,*args, **kwargs):
#         id=kwargs.get("pk")
#         form=TodosForm(request.POST, instance=id)
#         if form.is_valid():
#             Todos.objects.filter(**form.cleaned_data)
#             return redirect("all-todo")
#         return render(request,'edit.html',{"form":form})


class TaskTrueView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")  
        Todos.objects.filter(id=id).update(status=True)    
        return redirect('all-todo')  


class CompletedTodos(View):
    def get(self,request,*args, **kwargs):
        qs=Todos.objects.filter(status=True)
        return render(request,'completed.html',{"todos":qs})
    
class RegistrationView(FormView):
    def get(self,request,*args, **kwargs):
        form=RegistrationForm()
        return render(request,'register.html',{"form":form})
  