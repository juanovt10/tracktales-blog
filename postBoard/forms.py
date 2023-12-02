from .models import Post, TAGS, WORLD_AREAS, Comment
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


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "cols": "100", 
                "rows":"3",
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('body',)


class ProfileForm(forms.ModelForm):
    display_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    user_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "cols": "100", 
                "rows":"3",
            }
        )
    )
    most_visited_area = forms.ChoiceField(
        widget=forms.Select(
            attrs= {"class": "btn btn-secondary dropdown-toggle"}),
        choices=WORLD_AREAS,
    )
    languages = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    countries_traveled = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Comment
        fields = ('display_name', 'user_description', 'most_visited_area', 'languages', 'countries_traveled')
