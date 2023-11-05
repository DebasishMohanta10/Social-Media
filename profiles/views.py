from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
# from django.views.generic import DetailView
from django.contrib.auth.models import User
from .forms import EditProfileForm,EditUserForm
from feed.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    user_form = EditUserForm(instance=request.user)
    profile_form = EditProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = EditUserForm(request.POST,instance=request.user)
        profile_form = EditProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if all([user_form.is_valid(),profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('profile_detail',kwargs={"username": request.user.username}))
        
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request,"profiles/edit_profile.html",context)

# class ProfileDetailView(DetailView):
#     http_method_names = ["get"]
#     template_name = "profiles/detail.html"
#     model = User
#     context_object_name = "user"
#     slug_field = "username"
#     slug_url_kwarg = "username"

def profile_detail_view(request,username):
    user = get_object_or_404(User, username=username)
    followers_list = [u.followed_by.id for u in user.following.all()]
    # print(followers_list)
    context = {
        "user": user,
        "followers_list": followers_list
    }
    return render(request,"profiles/detail.html",context)

def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by("-id")
    return render(request,"feed/index.html",{"posts":posts})