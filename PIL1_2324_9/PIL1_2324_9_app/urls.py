# main/urls.py
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, ProfileViewSet, MatchViewSet, MessageViewSet, AdminViewSet, UserActionViewSet, PasswordResetViewSet, InterestViewSet, UserInterestViewSet, FilterViewSet, ProfilePictureViewSet
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'profiles', ProfileViewSet)
# router.register(r'profile_pictures', ProfilePictureViewSet)
# router.register(r'matches', MatchViewSet)
# router.register(r'messages', MessageViewSet)
# router.register(r'admins', AdminViewSet)
# router.register(r'user_actions', UserActionViewSet)
# router.register(r'password_resets', PasswordResetViewSet)
# router.register(r'interests', InterestViewSet)
# router.register(r'user_interests', UserInterestViewSet)
# router.register(r'filters', FilterViewSet)
# from django.contrib.auth import views
from PIL1_2324_9_app import views
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

urlpatterns = [
   path('register/', views.register_view, name='register'),
   path('login/', views.login_view, name='login'),
   path('profile/', views.profile_view, name='profile'),
   path('configuration/', views.configuration_view, name='configuration'),
   path('logout/', views.logout_view, name='logout'),
   path('', views.home, name='home'),
    # path('friends/', views.friends_list, name='friends_list'),
    # path('friends/send_request/<int:user_id>/', views.send_
    # friend_request, name='send_friend_request'),
    # path('friends/accept_request/<int:friendship_id>/', views.accept_friend_request, name='accept_friend_request'),
    # path('chat/<str:friend_username>/', views.chat_room, name='chat_room'),  
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
# from django.urls import include, path
# from django.contrib.auth import views as auth_views
# from .views import CustomPasswordResetView
# urlpatterns = [
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('profile/', views.profile_view, name='profile'),
#     path('logout/', views.logout_view, name='logout'),
#     path('', views.home, name='home'),
#     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     # path('reset_password', views.PasswordResetView.as_view(),name='reset_password'),
#     # path('reset_password_send', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     # path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
#     # path('reset_password_complete', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
#     #path('', include(router.urls)),
# ]

    # path('',views.login,name='login'),
    # path('register/',views.register,name='register'),
    

