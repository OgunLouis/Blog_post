from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.post_list, name='post_list'), #list view
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # detail view
    path('post/new/', views.post_create, name='post_create'), #create new post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('signup/', views.register_view, name='signup'),
    



 # Auth
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),

]
