from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.TodoCreateView.as_view(),name='add-todo'),
    path("all/",views.TodoListView.as_view(),name='all-todo'),
    path('<int:pk>/',views.TodoDetailView.as_view(),name='todo-detail'),
    path('<int:pk>/remove/',views.TodoDeleteView.as_view(),name='delete'),
    path('<int:pk>/status/true/',views.TaskTrueView.as_view(),name='status'),
    path('completed/',views.CompletedTodos.as_view(),name='completed'),
    
    
    # path('<int:pk>/edit/',views.TodoUpdateView.as_view(),name='edit'),
    
]
