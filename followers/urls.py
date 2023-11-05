from django.urls import path
from .import views

urlpatterns = [
    path("<str:username>/follow",views.follow,name="follow"),
    path("<str:username>/unfollow",views.unfollow,name="unfollow"),
]