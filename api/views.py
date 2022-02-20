from re import L
from django.db.models.fields import mixins

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Profile,Movie,Cast,Company,Country,Language,Genre,Actor,Review
from .serializers import ActorSerializer, CountrySerializer,CompanySerializer, GenreSerializer
from .serializers import LanguageSerializer,ProfileSerializer,MovieSerializer,ReviewSerializer, CastSerializer

class UserWritePermission(BasePermission):
    '''User can only edit their profile. Only superuser can edit other profiles.'''
  
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_superuser or request.user == obj.user)

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_superuser)

class ProfileWritePermission(BasePermission):
    '''User can edit review from their profile only.'''

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            profile_id = request.user.id
            profile = Profile.objects.filter(user_id=profile_id)
            if profile:
                return bool((request.user and request.user.is_superuser) or profile == obj.profile)
            else:
                return bool(request.user and request.user.is_superuser)
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_superuser)

class IsSuperUser(BasePermission):
    ''' Allows access only to superusers.'''
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_superuser)

class ProfileViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,UserWritePermission,viewsets.GenericViewSet): 
    permission_classes = [UserWritePermission]
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

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
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer

class CastViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Cast.objects.all().order_by('id')
    serializer_class = CastSerializer

class CompanyViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

class CountryViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer

class LanguageViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Language.objects.all().order_by('id')
    serializer_class = LanguageSerializer

class ReviewViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [ProfileWritePermission]
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        '''Mapping profile field to profile of logged in user unless it's superuser editing existing review.'''

        if(self.request.user.is_superuser):
            serializer.save()
        else:
            profile = None
            if self.request and hasattr(self.request, 'user'):
                profile_id = self.request.user.id
                profile = Profile.objects.get(pk=profile_id)
            serializer.save(profile=profile)

class ActorViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer

class GenreViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,IsSuperUser,viewsets.GenericViewSet): 
    permission_classes = [IsSuperUser]
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
