from django.urls import path
from .views import index, PostBoard, CreateProfile, ProfileDetail, DeletePostView, EditPostView
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('board/', PostBoard.as_view(), name='post_board'),
    path('create_profile/<slug:username>/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/<slug:username>/', ProfileDetail.as_view(), name='profile-detail'),
    path('delete_post/', views.DeletePostView.as_view(), name='delete_post'),
    path('edit_post/<slug:slug>', views.EditPostView.as_view(), name='edit_post'),
]