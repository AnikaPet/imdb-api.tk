from lib2to3.pytree import Base
from django.contrib.auth.models import User
from django.db.models.fields import mixins
from django.http import HttpResponse
from django.shortcuts import render

from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profile,Movie,Cast,Company,Country,Language,Genre,Actor,Review
from .serializers import ActorSerializer, CountrySerializer,CompanySerializer, GenreSerializer, RegisterSerializer
from .serializers import LanguageSerializer,ProfileSerializer,MovieSerializer,ReviewSerializer, CastSerializer

class MoviesPermission(BasePermission):
    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated

class UserWritePermission(BasePermission):
    '''User can only edit their profile. Only superuser can edit other profiles.'''
  
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            else:
                return bool(request.user.is_superuser or request.user == obj.user)
        else:
            return False

    def has_permission(self, request, view):
        return request.user.is_authenticated

class ProfileWritePermission(BasePermission):
    '''User can edit review from their profile only.'''
    # obj is Review

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        else:
            user = request.user
            profile = Profile.objects.get(user_id=user.id)
            return bool(request.user.is_superuser or profile == obj.profile)
    
    def has_permission(self, request, view):
        return request.user


class IsSuperUser(BasePermission):
    ''' Allows access only to superusers.'''
    
    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_authenticated and request.user.is_superuser)

class RegisterUserViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.all().order_by('id')
    serializer_class = RegisterSerializer

class ProfileViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,UserWritePermission,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserWritePermission]
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        This view should return profile
        for the currently authenticated user.
        """
        user = self.request.user
        return Profile.objects.filter(user=user)

    def perform_create(self, serializer):
        '''Mapping user field to logged in user unless it's superuser editing existing profile.'''

        if(self.request.user.is_superuser):
            serializer.save()
        else:
            user = None
            if self.request and hasattr(self.request, 'user'):
                user = self.request.user
            serializer.save(user=user)

class MovieViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,MoviesPermission,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviesPermission]
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned movies to a given title and/or genre title.
        """
        queryset = Movie.objects.all()
        title = self.request.query_params.get('title')
        genre_title = self.request.query_params.get('genre_title')

        if genre_title and title is not None:
            queryset = queryset.filter(Q(genre__title__icontains=genre_title) and Q(title__icontains=title))
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if genre_title is not None:
            queryset = queryset.filter(genre__title__icontains=genre_title)
        return queryset

class CastViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Cast.objects.all().order_by('id')
    serializer_class = CastSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'movie_id'}

class CompanyViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

class CountryViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer

class LanguageViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Language.objects.all().order_by('id')
    serializer_class = LanguageSerializer

class ReviewViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,ProfileWritePermission,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [ProfileWritePermission]
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

    # Filter reviews by profile_id or movie_id
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'profile_id','movie_id'}

    def perform_create(self, serializer):
        '''Mapping profile field to profile of logged in user unless it's superuser editing existing review.'''

        if(self.request.user.is_superuser):
            serializer.save()
        else:
            profile = None
            if self.request.user:
                user = self.request.user
                profile = Profile.objects.get(user_id=user.id)
            serializer.save(profile=profile)

class ActorViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer

class GenreViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

'''Returning images.'''

def movie_image_view(request,  movie_id):
    image = Movie.objects.get(pk=movie_id).img
    return HttpResponse(image, content_type="image/png")

def actor_image_view(request,  actor_id):
    image = Actor.objects.get(pk=actor_id).img
    return HttpResponse(image, content_type="image/png")

'''Documentation and home page.'''

def about_us(request):
    '''A view of about us page.'''

    return render(request,'about_us.html')

def documents(request):
    return render(request,'documentation/docs.html')

def token_docs(request):
    return render(request,'documentation/token.html')

def actor_docs(request):
    return render(request,'documentation/actors.html')

def cast_docs(request):
    return render(request,'documentation/cast.html')

def company_docs(request):
    return render(request,'documentation/company.html')

def country_docs(request):
    return render(request,'documentation/country.html')

def genre_docs(request):
    return render(request,'documentation/genre.html')

def language_docs(request):
    return render(request,'documentation/language.html')

def movie_docs(request):
    return render(request,'documentation/movie.html')

def review_docs(request):
    return render(request,'documentation/review.html')

def profile_docs(request):
    return render(request,'documentation/profile.html')

def image_docs(request):
    return render(request,'documentation/image.html')