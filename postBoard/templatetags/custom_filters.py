from django import template
from postBoard.forms import EditPostForm

register = template.Library()

#filter for the like post display
@register.filter(name='user_liked_post')
def user_liked_post(post, user):
    return post.likes.filter(id=user.id).exists()

#filter for the comment post display
@register.filter
def key(d, key_name):
    return d[key_name]

@register.filter(name='edit_post')
def edit_post(post, *fields):
    form = EditPostForm(instance=post, prefix=f'post_form_edit_{post.slug}')
    return [form[field] for field in fields]