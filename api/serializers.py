from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Profile,Movie,Cast,Company,Country,Language,Genre,Actor,Review

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])   
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = []

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        exclude = []

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = []

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = []

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = []

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = []

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = []

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['profile']