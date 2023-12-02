from django.urls import path
from .views import index, PostBoard, CreateProfile
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('board/', PostBoard.as_view(), name='post_board'),
    path('create_profile/<str:username>', views.CreateProfile.as_view(), name='create_profile')
]