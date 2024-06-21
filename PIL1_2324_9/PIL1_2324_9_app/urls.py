# main/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, MatchViewSet, MessageViewSet, AdminViewSet, UserActionViewSet, PasswordResetViewSet, InterestViewSet, UserInterestViewSet, FilterViewSet, ProfilePictureViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'profile_pictures', ProfilePictureViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'user_actions', UserActionViewSet)
router.register(r'password_resets', PasswordResetViewSet)
router.register(r'interests', InterestViewSet)
router.register(r'user_interests', UserInterestViewSet)
router.register(r'filters', FilterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
