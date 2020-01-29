from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.utils import timezone
from django import forms
from .forms import PostForm, UserProfileForm
from .models import Post
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your views here.

def post_list(request) :
    posts = Post.objects.order_by('cost')
    return render(request, 'blog/post_list.html', {'posts' : posts})


def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})


@login_required
def post_new(request) :
    if request.method == "POST" :
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})


@login_required
def post_edit(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST" :
        form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})


@login_required
def post_remove(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


@login_required
def post_open(request) :
    return render(request, 'blog/post_open.html', {})


@login_required
def post_update(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    coll = get_user_model()
    return render(request, 'blog/post_update.html', coll)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('post_list')
    else:
        form = UserCreationForm()
        profile_form = UserProfileForm()
        args = {'form': form, 'profile_form': profile_form}
        return render(request, 'blog/register.html', args)



