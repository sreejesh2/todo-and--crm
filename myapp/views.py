from django.shortcuts import render, redirect
from .models import Todos
from .forms import TodosForm, RegistrationForm, LoginForm
from django.views.generic import View, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


class TodoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TodosForm()
        return render(request, "todo-create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TodosForm(request.POST)
        if form.is_valid():
            Todos.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"Todo has been created successfully")
            return redirect('all-todo')
        messages.error(request,"faild todo create")
        return render(request, 'todo-create.html', {"form": form})


class TodoListView(View):
    def get(self, request, *args, **kwargs):

        qs = Todos.objects.filter(user=request.user).order_by("-date")
        return render(request, 'todo-list.html', {"todos": qs})


class TodoDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = Todos.objects.get(id=id)
        context = {"todo": qs}
        return render(request, 'todo-detail.html', context)


class TodoDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        Todos.objects.get(id=id).delete()
        messages.success(request,"Deleted todo")
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
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        Todos.objects.filter(id=id).update(status=True)
        return redirect('all-todo')


class CompletedTodos(View):
    def get(self, request, *args, **kwargs):
        qs = Todos.objects.filter(status=True)
        return render(request, 'completed.html', {"todos": qs})


class RegistrationView(FormView):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successfully")
            return redirect('login')
        messages.error(request,"Please enter correct details")
        return render(request, 'register.html', {"form": form})


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')
            usr = authenticate(request, username=uname, password=psw)
            if usr:
                login(request, user=usr)
                messages.success(request,"")
                return redirect('all-todo')
        messages.error(request,"Invaid credentials")
        return render(request, 'login.html', {"form": form})


def signout_view(request,*args, **kwargs):
    logout(request)
    return redirect("login")