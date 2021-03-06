from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_list/', views.create_list, name="create_list"),
    path('complete/<int:id>/', views.complete_todo, name="complete_todo"),
    path('delete/<int:id>/', views.delete_todo, name="delete_todo"),
]