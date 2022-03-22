from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('list/', views.index, name='list'),
    path('create_task/', views.createTask, name='create-task'),
    path('update/<str:pk>/', views.updateToDoApp, name='update'),
    path('delete/<str:pk>/', views.deleteTodo, name='delete'),
    path('view_todo/<str:pk>/', views.viewToDoList, name='view-todo'),
]