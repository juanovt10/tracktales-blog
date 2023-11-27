from .models import Post, TAGS, WORLD_AREAS
from django import forms


class PostForm(forms.ModelForm):
    tags = forms.ChoiceField(
        widget=forms.Select,
        choices=TAGS 
    )
    world_area = forms.ChoiceField(
        widget=forms.Select,
        choices=WORLD_AREAS  
    )
    country = forms.CharField()
    post_content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('author', 'tags', 'world_area', 'country', 'content',)
    

   

