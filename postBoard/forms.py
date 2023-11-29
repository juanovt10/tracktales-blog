from .models import Post, TAGS, WORLD_AREAS
from django import forms
from django.utils.html import format_html
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    country = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    tags = forms.ChoiceField(
        widget=forms.Select(
            attrs= {
                "class": "btn btn-secondary dropdown-toggle",
                "placeholder": "Holiday Type",
            }
        ),
        choices=TAGS,
    )

    world_area = forms.ChoiceField(
        widget=forms.Select(
            attrs= {"class": "btn btn-secondary dropdown-toggle"}),
        choices=WORLD_AREAS,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "cols": "100", 
                "rows":"3",
            }
        )
    )
    class Meta:
        model = Post
        fields = ('tags', 'title', 'world_area', 'country', 'content',)
   
   

