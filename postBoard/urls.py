from django.urls import path
from .views import index, PostBoard


urlpatterns = [
    path('', index, name='index'),
    path('board/', PostBoard.as_view(), name='post_board'),
]