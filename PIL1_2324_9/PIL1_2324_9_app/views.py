from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Profile, Match, Message, Admin, UserAction, PasswordReset, Interest, UserInterest, Filter, ProfilePicture
from .serializers import UserSerializer, ProfileSerializer, MatchSerializer, MessageSerializer, AdminSerializer, UserActionSerializer, PasswordResetSerializer, InterestSerializer, UserInterestSerializer, FilterSerializer,ProfilePictureSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class ProfilePictureViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilePictureSerializer
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class UserActionViewSet(viewsets.ModelViewSet):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

class PasswordResetViewSet(viewsets.ModelViewSet):
    queryset = PasswordReset.objects.all()
    serializer_class = PasswordResetSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class UserInterestViewSet(viewsets.ModelViewSet):
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
class ProfilePictureViewSet(viewsets.ModelViewSet):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer
""" from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse """
# Create your views here.
#def home(request):
    #return  HttpResponse("<h2>Welcome to my app</h2>")#render(request,'index.html')
""" template = loader.get_template('home.html')
    return HttpResponse(template.render())
 """
# main/views.py

