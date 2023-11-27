from .models import Post, TAGS, WORLD_AREAS
from django import forms

class PostForm(forms.ModelForm):
    # class Meta:
    #     model = Post
    #     fields = ('title', 'tags', 'world_area', 'country', 'content',)
    username = forms.CharField()
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