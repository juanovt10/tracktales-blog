from .models import Post, TAGS, WORLD_AREAS, Comment, UserProfile, ContactInfo
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}), required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter country"}), required=True)
    tags = forms.ChoiceField(
        widget=forms.Select(
            attrs= {
                "class": "btn btn-info dropdown-toggle",
            }
        ),
        choices=TAGS,
        required=True,
    )

    world_area = forms.ChoiceField(
        widget=forms.Select(
            attrs= {"class": "btn btn-info dropdown-toggle"}),
        choices=WORLD_AREAS,
        required=True,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "cols": "100", 
                "rows":"3",
                "placeholder": "Describe your experience!"
            }
        ), 
        required=True,
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
                "placeholder": "Add your comment here!"
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
            attrs= {"class": "btn btn-info dropdown-toggle"}),
        choices=WORLD_AREAS,
    )
    languages = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    countries_traveled = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control", "type":"number"}))

    class Meta:
        model = UserProfile
        fields = ('display_name', 'user_description', 'most_visited_area', 'languages', 'countries_traveled')


class ContactUsForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "cols": "100", 
                "rows":"3",
            }
        ),
        required=True
    )
    class Meta:
        model = ContactInfo
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'subject', 'message',)
        