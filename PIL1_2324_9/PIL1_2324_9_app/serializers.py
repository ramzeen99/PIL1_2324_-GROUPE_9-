# main/serializers.py

from rest_framework import serializers
from .models import User, Profile, Match, Message, Admin, UserAction, PasswordReset, Interest, UserInterest, Filter, ProfilePicture

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ['id', 'image','uploaded_at']
class UserSerializer(serializers.ModelSerializer):
    profile_pictures = ProfilePictureSerializer(many=True, read_only=True)        
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_of_birth', 'gender', 'location','profile_pictures', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    """ def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user """

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = '__all__'

class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class UserInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterest
        fields = '__all__'

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'
