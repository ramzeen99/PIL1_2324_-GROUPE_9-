from django.db import models
from django.contrib.auth.models import AbstractUser , Permission,BaseUserManager
from django.utils.translation import gettext_lazy as _
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('H', 'Homme'), ('F', 'Femme'), ('A', 'Autre')], null=True, blank=True)
    interested_in = models.CharField(max_length=1, choices=[('H', 'Homme'), ('F', 'Femme'), ('T', 'Tout')], null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    age = models.IntegerField(default=12)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False)
    def get_friends(self):
        friends = set()
        for friendship in Friendship.objects.filter(from_user=self):
            friends.add(friendship.to_user)
        for friendship in Friendship.objects.filter(to_user=self):
            friends.add(friendship.from_user)
        return friends
    def get_friend_requests(self):
        return Friendship.objects.filter(to_user=self, accepted=False)
class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='friendship_creator_set', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    class Meta:
        unique_together = ('from_user', 'to_user')

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    preferred_age_range = models.CharField(max_length=10, null=True, blank=True)
    preferred_location = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
class ProfilePicture(models.Model):
    user = models.ForeignKey(User, related_name='profile_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')
    # user = models.ForeignKey(User, related_name='profile_pictures', on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='profile_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Match(models.Model):
    user1 = models.ForeignKey(User, related_name='matches_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='matches_as_user2', on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)

# class Message(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
#     receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     sent_at = models.DateTimeField(auto_now_add=True)

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

# Create your models here.
