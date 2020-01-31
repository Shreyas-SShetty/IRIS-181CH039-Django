# views connect models with templates .

from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.utils import timezone
from django import forms
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your views here.

# Function returns post_list.html that contains the homepage
# Request :GET
def post_list(request) :
    posts = Post.objects.order_by('cost')
    return render(request, 'blog/post_list.html', {'posts' : posts})



# Function returns post_deatil.html that contains the description of a particular object
# Request :GET
def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})



# Requests template to add a new object
# Request :POST
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




# Requests template to edit an existing object 
# Request :PUT
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




# Requests template for delete
# Request :DELETE
@login_required
def post_remove(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



#Requests template for displaying error message
# Request: GET
@login_required
def post_open(request) :
    return render(request, 'blog/post_open.html', {})



# Request: GET
@login_required
def post_update(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    coll = get_user_model()
    return render(request, 'blog/post_update.html', coll)



# Requests template for adding new user
# Requests=: POST
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            return redirect('post_list')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'blog/register.html', args)
