from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from followers.models import Follower
# class HomePage(ListView):
#     template_name = 'feed/index.html'
#     model = Post
#     context_object_name = "posts"
#     queryset = Post.objects.all().order_by('-id')[0:30]
@login_required
def home_page(request):
    if request.user.is_authenticated:
        if request.user.followed_by.count() >= 1:
            following = [u.following.id for u in request.user.followed_by.all()]
            posts = Post.objects.filter(author__in=following).order_by("-id")
            if len(posts) == 0:
                return redirect(reverse("follow_users"))
        else:
            # render a page to follow people
            return redirect(reverse("follow_users"))
    else:
        posts = Post.objects.all().order_by('-id')[:30]
    return render(request,'feed/index.html',{'posts':posts})

@login_required
def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(reverse('post_detail',kwargs={"pk": post.id}))
    context = {"form": form,"post": post}
    return render(request,"feed/detail.html",context)
# class PostDetailView(LoginRequiredMixin,DetailView):
#     template_name="feed/detail.html"
#     model = Post
#     context_object_name = "post"

class CreateNewPost(LoginRequiredMixin,CreateView):
    template_name = "feed/create.html"
    model = Post
    fields = ["title","text"]
    success_url = "/"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

@login_required
def follow_users(request):
    users = User.objects.exclude(username=request.user.username).exclude(username="admin")
    # users followed by 
    f = Follower.objects.filter(followed_by=request.user)
    print(f)
    followed_users = [u.following.id for u in f]
    context = {"users": users,"followed_users": followed_users}
    return render(request,"feed/follow_users.html",context)