from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class User(AbstractUser):
    name = models.CharField(max_length=25, blank=True)
    surname = models.CharField(max_length=25, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_id = User.id
    bio = models.TextField(null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    preferred_age_range = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    preferred_location = models.CharField(max_length=100, null=True, blank=True)
    preferred_gender = models.CharField(max_length=10, null=True, blank=True)
    

class ProfilePicture(models.Model):
    user = models.ForeignKey(User, related_name='profile_pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Match(models.Model):
    user1 = models.ForeignKey(User, related_name='matches_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='matches_as_user2', on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_admin = models.BooleanField(default=False)

class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    action_date = models.DateTimeField(auto_now_add=True)

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

class Filter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age_range = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
