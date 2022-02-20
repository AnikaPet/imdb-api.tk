from rest_framework import serializers
from .models import Profile,Movie,Cast,Company,Country,Language,Genre,Actor,Review

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