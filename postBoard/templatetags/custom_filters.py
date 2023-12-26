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

#filter to display custom date
@register.filter(name='custom_timesince')
def custom_timesince(value):
    timesince_str = timesince(value)
    parts = timesince_str.split(', ')

    amount = parts[0].replace('\xa0', ' ').split()[0]
    unit = parts[0].replace('\xa0', ' ').split()[1].lower()

    if unit in ['minute', 'minutes', 'hour', 'hours', 'day', 'days', 'week', 'weeks', 'year', 'years']:
        return f"{amount}{unit[0]}"