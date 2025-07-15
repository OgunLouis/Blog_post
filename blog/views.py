from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib.auth import login
from .forms import RegisterForm
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # This shows the newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#To create posts
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_detail', pk=new_post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

#To Edit Posts
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})

#To delete post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


#To Signup
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in right after signup
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

#Create the Profile View
from .models import Profile
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'blog/user_profile.html', {'profile_user': user})



#To edit user profile
@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'blog/edit_profile.html', {'form': form})
