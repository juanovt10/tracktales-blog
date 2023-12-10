from django import template
from django.utils.timesince import timesince

register = template.Library()

#filter for the like post display
@register.filter(name='user_liked_post')
def user_liked_post(post, user):
    return post.likes.filter(id=user.id).exists()

#filter for the comment post display
@register.filter
def key(d, key_name):
    return d[key_name]

@register.filter(name='custom_timesince')
def custom_timesince(value):
    timesince_str = timesince(value)
    print(timesince_str)
    parts = timesince_str.split(', ')
    print(parts)
    if len(parts) > 1:
        long_ago = parts[0][:-6]
        return long_ago + 'h'
    else: 
        if timesince_str == '1 minute':
            long_ago = timesince_str[:-7]
        else: 
            long_ago = timesince_str[:-8]
        return long_ago + 'm'