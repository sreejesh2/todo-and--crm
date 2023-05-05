from rest_framework import serializers

from crm.models import Employee

class EmployeeSerilizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields="__all__"