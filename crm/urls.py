from django.urls import path
from . import views

urlpatterns = [
    
   path('add/',views.EmployeeCreateView.as_view(),name='erp-add'),
   path('all/',views.EmployeeListView.as_view(),name='erp-list'),
   path('<int:pk>/',views.EmployeeDetailView.as_view(),name='emp-detail'),
   path('<int:pk>/edit/',views.EmployeeEditView.as_view(),name='emp-edit'),
   path('<int:pk>/delete/',views.EmployeeDeleteView.as_view(),name='emp-delete'),

]
