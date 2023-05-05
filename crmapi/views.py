from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from crm.models import Employee
from .serilizer import EmployeeSerilizer


class EmployeeView(ViewSet):
    #localhost:8000/api/employees/
    #method get
    def list(self,request,*args, **kwargs):
        qs=Employee.objects.all()
        if "department" in request.query_params:
            dept=request.query_params.get("department")
            qs=qs.filter(department__iexact=dept)

        if "gender" in request.query_params:
            gen=request.query_params.get("gender")
            qs=qs.filter(gender__iexact=gen) 

        if "salary" in request.query_params:
            sal=request.query_params.get("salary")
            qs=qs.filter(salary__iexact=sal)   

        if "salary_gt" in request.query_params:
            sal=request.query_params.get("salary_gt")
            qs=qs.filter(salary__gte=sal)       

        serilizer=EmployeeSerilizer(qs,many=True)
        return Response(data=serilizer.data)
    
    #localhost:8000/api/employees/
    #method post
    def create(self,request,*args, **kwargs):
        serilizer=EmployeeSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)
    
    
    #localhost:8000/api/employees/1/
    #method get
    def retrieve(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        serilizer=EmployeeSerilizer(qs)
        return Response(data=serilizer.data)
    
    #localhost:8000/api/employees/1/
    #method put
    def update(self,request,*args, **kwargs):
        id = kwargs.get("pk")
        emp_obj=Employee.objects.get(id=id)
        serializer=EmployeeSerilizer(instance=emp_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    

    #localhost:8000/api/employees/1/
    #method delete
    def destroy(self,request,*args, **kwargs):
        try:
            id = kwargs.get("pk")
            Employee.objects.get(id=id).delete()
            return Response(data="deleted success full")
        except Exception:
            return Response(data="no maching record found")
        

    @action(methods=["get"],detail=False)
    def departments(self,request,*args, **kwargs):
        qs=Employee.objects.all().values_list('department',flat=True).distinct()
        print(qs)
        return Response(data=qs)

class EmployeeViewsetView(ModelViewSet):
    serializer_class=Employee
    model=Employee
    queryset=Employee.objects.all()        