from django.urls import path
from client import views

urlpatterns = [
    path('posts', views.PostsView.as_view()),

]
