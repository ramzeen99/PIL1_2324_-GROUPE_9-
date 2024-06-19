from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import User, Profile, Match, Message, Admin, UserAction, PasswordReset, Interest, UserInterest, Filter, ProfilePicture
from .forms import *
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
def customize(request):
    logged_user = get_logged_user_from_request(request)
    if not logged_user:
        return redirect('login')
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.instance.user = logged_user
            form.save()
            return redirect('home')
    return render(request,'customize.html' ,{'form':form })
def show_profile(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if 'userToShow' in request.GET and request.GET['userToShow'] != '':
            user_to_show_id = int(request.GET['userToShow'])
            results = Profile.objects.filter(user_id=user_to_show_id)
            if len(results) == 1:
                user_to_show = Profile.objects.get(user_id=user_to_show_id)
                return render(request, 'show_profile.html',{'user_to_show':user_to_show})
            else:
                return render(request, 'show_profile.html',{'user_to_show':logged_user})
        else:
            return render(request, 'show_profile.html',{'user_to_show':logged_user})
    else:
        return redirect('login')
                
                


def modify_profile(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if len(request.GET) > 0:
            form = ProfileForm(request.GET, instance=logged_user)
            
            if form.is_valid():
                print("ok")
                form.save()
                return redirect('home')
            else:
                return render(request, 'modify_profile.html', {'form':form})
        else:
            form = ProfileForm(request.GET, instance=logged_user)

            return render(request, 'modify_profile.html', {'form':form})
    else:
        return redirect('/login')
    

