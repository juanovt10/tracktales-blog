from django.contrib import admin
from .models import Post, Comment, UserProfile, ContactInfo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'slug', 'approved', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved', 'created_on', 'tags')
    actions = ['approved_post']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('body', 'author', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('username', 'display_name', 'created_on', 'approved')
    list_filter = ('username', 'created_on')
    search_fields = ('username', 'display_name')
    actions = ['approve_profile']


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'subject', 'message')
    list_filter = ('last_name',)
    search_fields = ('last_name', 'email')

