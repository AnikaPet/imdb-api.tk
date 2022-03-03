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

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = []

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    class Meta:
        model = Movie
        exclude = []

class ProfileSerializer(serializers.ModelSerializer):
    saved_movies = MovieSerializer(read_only=True,many=True)
    class Meta:
        model = Profile
        exclude = ['user']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = []

class CastSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(read_only=True)
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


class ReviewSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        exclude = []