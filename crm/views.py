from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

# ======employee create view===========

class EmployeeCreateView(View):
    def get(self,request,*args, **kwargs):
        form=EmployeeForm()
        return render(request,'erp-add.html',{"form":form})
    
    def post(self,request,*args, **kwargs):
        form=EmployeeForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('erp-list')
        return render(request,'erp-add.html',{"form":form})
    
    
    
#=======employeee listview========
class EmployeeListView(View):
    def get(self,request,*args, **kwargs):
        qs= Employee.objects.all()
        return render(request,'erp-list.html',{"employee":qs})
    


class EmployeeDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,'emp-detail.html',{"employee":qs})  



class EmployeeEditView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        emp=Employee.objects.get(id=id)
        form=EmployeeForm(instance=emp)         
        return render(request,'emp-edit.html',{"form":form})
    
    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        emp=Employee.objects.get(id=id)
        form=EmployeeForm(request.POST,files=request.FILES,instance=emp)
        if form.is_valid():
            form.save()
            return redirect("emp-detail",pk=id)
        return render(request,'emp-edit.html',{"form":form})
    
class EmployeeDeleteView(View):
    def get(self,request,*args, **kwargs):
        id= kwargs.get("pk")  
        Employee.objects.get(id=id).delete() 
        return redirect('erp-list') 
