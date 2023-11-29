from .models import Post, TAGS, WORLD_AREAS
from django import forms
from django.utils.html import format_html



def add_class_to_option(choice, css_class):
    return (choice[0], format_html('<option class="{}">{}</option>', css_class, choice[1]))

# Construct choices with added class
TAGS_WITH_CLASSES = [add_class_to_option(choice, 'dropdown-item') for choice in TAGS]

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
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "cols": "100", 
                "rows":"5",
            }
        )
    )
    class Meta:
        model = Post
        fields = ('author', 'tags', 'title', 'world_area', 'country', 'content',)
   
   

