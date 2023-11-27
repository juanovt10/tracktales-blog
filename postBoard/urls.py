from django.urls import path
from .views import index, PostBoard, create_post


urlpatterns = [
    path('', index, name='index'),
    path('board/', PostBoard.as_view(), name='post_board'),
    path('create_post', create_post, name='create_post'),
]