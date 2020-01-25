from django import forms

from .models import Post


class PostForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ('name', 'image', 'description', 'age', 'cost', 'address', 'seller', 'phone',)
