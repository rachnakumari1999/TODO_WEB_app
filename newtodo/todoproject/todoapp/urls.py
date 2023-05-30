from django.urls import path
from todoapp import views 

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.Create_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]