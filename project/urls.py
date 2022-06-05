from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('',views.projects,name='projects'),
    #path('panda/',views.panda,name='panda1'),
    path('panda/<str:pk>/',views.panda,name='panda'),
    path('create-project/',views.createproject,name="create-project"),
    path('update-project/<str:pk>/',views.updateproject,name="update-project"),
    path('delete-project/<str:pk>/',views.deleteproject,name="delete-project"),
]