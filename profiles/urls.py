from django.urls import path

from . import views

urlpatterns = [
    path("profile/<str:username>",views.profile_detail_view,name="profile_detail"),
    path("profile/me/edit",views.edit_profile,name="edit_profile"),
    path("myposts/",views.my_posts,name="my_posts")
]