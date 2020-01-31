from django import forms
from .models import UserProfile
from .models import Post
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ['name', 'image', 'description', 'years', 'months', 'days', 'cost', 'address', 'seller', 'phone', ]
