from django.urls import path
from .views import index, about_us, contact_success, PostBoard, CreateProfile, ProfileDetail, DeletePostView, ContactUs, account_signup_redirect
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('board/', PostBoard.as_view(), name='post_board'),
    path('account_signup_redirect/', account_signup_redirect, name='account_signup_redirect'),
    path('create_profile/<slug:username>/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/<slug:username>/', ProfileDetail.as_view(), name='profile_detail'),
    path('delete_post/', views.DeletePostView.as_view(), name='delete_post'),
    path('contact_us/', views.ContactUs.as_view(), name='contact_us'),
    path('contact_success/', contact_success, name='contact_success'),
]