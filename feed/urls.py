from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page,name='index'),
    path("feed/",views.home_page,name='home'),
    path("feed/<int:pk>",views.post_detail,name='post_detail'),
    path("feed/new/",views.CreateNewPost.as_view(),name="new_post"),
    path("follow-known/",views.follow_users,name="follow_users")
]