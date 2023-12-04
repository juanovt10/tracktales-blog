from django.urls import path
from .views import index, PostBoard, CreateProfile, ProfileDetail
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('board/', PostBoard.as_view(), name='post_board'),
    path('create_profile/<slug:username>/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/<slug:username>/', ProfileDetail.as_view(), name='profile-detail'),
    # path('delete/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post')
]