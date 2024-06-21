from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template import loader
from django.utils.dateparse import parse_date
from .models import User, ProfilePicture
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
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
# Create your views here.
# def register(request):
#     template = loader.get_template('register.html')
#     return HttpResponse(template.render())
def home(request):
     #return  HttpResponse("<h2>Welcome to my app</h2>")#render(request,'index.html')
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    return render(request, 'home.html')
User = get_user_model()
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from .models import User
def generate_username(email):
    # Générer un username unique basé sur l'email
    username_base = email.split('@')[0]
    username = username_base
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f"{username_base}{counter}"
        counter += 1
    return username
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Valider les données du formulaire
        errors = []
        if password1 != password2:
            errors.append("Les mots de passe ne correspondent pas.")

        # if User.objects.filter(username=username).exists():
        #     errors.append("Le nom d'utilisateur est déjà pris.")

        if User.objects.filter(email=email).exists():
            errors.append("L'adresse email est déjà utilisée.")

        if errors:
            return render(request, 'home.html', {'errors': errors})
# Générer un username
        username = generate_username(email)
        # Créer l'utilisateur
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password1)
        )

        # Connecter l'utilisateur et rediriger
        login(request, user)
        return redirect('configuration')

    return render(request, 'home.html')
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Vérifie si l'utilisateur est un administrateur
                return redirect('/admin/')  # Redirige vers l'interface d'administration
            else:
                #return redirect('profile')  # Redirige vers la page de profil
                return redirect('profile')
        else:
            return render(request, 'home.html', {'error': 'Adresse email ou mot de passe incorrect.'})
    return render(request, 'home.html')
@csrf_protect
@login_required
def configuration_view(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST.get('first_name')
        birth_day = request.POST.get('birth_day')
        birth_month = request.POST.get('birth_month')
        birth_year = request.POST.get('birth_year')
        gender = request.POST.get('gender')
        interested_in = request.POST.get('interested_in')
        if birth_day and birth_month and birth_year:
            try:
                birth_date = f"{birth_year}-{birth_month.zfill(2)}-{birth_day.zfill(2)}"
                user.birth_date = birth_date
            except ValueError:
                # Gérer l'erreur de format de date ici
                pass
        # Mise à jour des informations utilisateur
        user.first_name = first_name
        user.gender = gender
        user.interested_in = interested_in
        user.save()

         # Sauvegarde des photos de profil
        for i in range(1, 7):
            photo = request.FILES.get(f'pdp{i}')
            if photo:
                ProfilePicture.objects.create(user=user, photo=photo)

        return redirect('friends_list')  # Redirige vers la page de profil après la sauvegarde


    return render(request, 'configuration/config.html', {'user': request.user})

def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.date_of_birth = request.POST.get('date_of_birth')
        user.gender = request.POST.get('gender')
        user.location = request.POST.get('location')
        user.save()
        return redirect('profile')
    return render(request, 'profile.html', {'user': request.user})
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Message, Friendship
from django.contrib.auth.decorators import login_required
# @login_required
# def friends_list(request):
#     friends = request.user.get_friends()
#     friend_requests = request.user.get_friend_requests()
#     users = User.objects.exclude(id=request.user.id)
#     return render(request, 'friends_list.html', {
#         'friends': friends,
#         'friend_requests': friend_requests,
#         'users': users,
#      })    
# @login_required
# def send_friend_request(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     friendship, created = Friendship.objects.get_or_create(from_user=request.user, to_user=user)
#     if created:
#         # Friendship request was sent
#         pass
#     return redirect('friends_list')

# @login_required
# def accept_friend_request(request, friendship_id):
#     friendship = get_object_or_404(Friendship, id=friendship_id)
#     if friendship.to_user == request.user:
#         friendship.accepted = True
#         friendship.save()
#     return redirect('friends_list')

# @login_required
# def chat_room(request, friend_username):
#     friend = get_object_or_404(User, username=friend_username)
#     return render(request, 'chat_room.html', {'friend': friend})


def logout_view(request):
    logout(request)
    return redirect('login')
def csrf_failure(request, reason=""):
    return render(request, 'csrf_failure.html', status=403) 
# views.py

from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password_reset/done/'
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = '/reset/done/'
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

# from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Command(BaseCommand):
#     help = 'Vérifie et met à jour les utilisateurs sans nom d\'utilisateur'

#     def handle(self, *args, **kwargs):
#         users_without_username = User.objects.filter(username='')
#         for user in users_without_username:
#             user.username = f'user_{user.id}'
#             user.save()
#         self.stdout.write(self.style.SUCCESS('Tous les utilisateurs ont un nom d\'utilisateur.'))

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Adresse email ou mot de passe incorrect.'})
#     return render(request, 'login.html')

# def register_view(request):
#     print("Request method:", request.method)  # Debug print
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         print("Form POST data:", request.POST)  # Debug print
#         if form.is_valid():
#             print("Form is valid")  # Debug print
#             user = form.save()
#             login(request, user)
#             return redirect('login')
#         else:
#             print("Form is not valid")  # Debug print
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})


# def inscription(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirige vers une page d'accueil après l'inscription
# # main/views.py
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})   
    
