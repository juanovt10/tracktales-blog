from .models import Post, TAGS, WORLD_AREAS
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'tags', 'title', 'world_area', 'country', 'content',)
   

