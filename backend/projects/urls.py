from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListCreate.as_view(), name="project-list"),
    path("delete/<int:pk>/", views.ProjectDelete.as_view(), name="project-delete"), #<int:pk> - pk od primary key
]