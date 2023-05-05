from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("employee",views.EmployeeView,basename="employees")
router.register('v1/employee',views.EmployeeViewsetView,basename='emp')

urlpatterns = [
  
    
]+router.urls