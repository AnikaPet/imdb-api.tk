from django.db.models.fields import mixins
from rest_framework import mixins
from rest_framework import viewsets

from .models import Profile,Movie,Cast,Company,Country,Language,Genre,Actor,Review
from .serializers import ActorSerializer, CountrySerializer,CompanySerializer, GenreSerializer
from .serializers import LanguageSerializer,ProfileSerializer,MovieSerializer,ReviewSerializer, CastSerializer
                           
class ProfileViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class MovieViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer

class CastViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Cast.objects.all().order_by('id')
    serializer_class = CastSerializer

class CompanyViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

class CountryViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer

class LanguageViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Language.objects.all().order_by('id')
    serializer_class = LanguageSerializer

class ReviewViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

class ActorViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer

class GenreViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
