from django.shortcuts import render,get_object_or_404,redirect
from .models import Follower
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

def follow(request,username):
    if request.user:
        user = get_object_or_404(User,username=username)
        if request.user != user:
            Follower.objects.create(followed_by=request.user,following=user)
        return redirect(reverse('profile_detail',kwargs={"username": username}))



def unfollow(request,username):
    if request.user:
        user_to_unfollow = get_object_or_404(User, username=username)
        if request.user != user_to_unfollow:
            Follower.objects.filter(followed_by=request.user, following=user_to_unfollow).delete()
        return redirect(reverse('profile_detail',kwargs={"username": username}))
