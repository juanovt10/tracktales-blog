from django.contrib import admin
from .models import Post, Tag, Comment, UserProfile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'slug', 'approved', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved', 'created_on', 'type_tags')
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