from django.contrib.auth.models import User
from django.db.models.fields import mixins

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny

from .models import Profile,Movie,Cast,Company,Country,Language,Genre,Actor,Review
from .serializers import ActorSerializer, CountrySerializer,CompanySerializer, GenreSerializer, RegisterSerializer
from .serializers import LanguageSerializer,ProfileSerializer,MovieSerializer,ReviewSerializer, CastSerializer

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

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            else:
                user_id = request.user.id
                profile = Profile.objects.get(user_id=user_id)
                profile_id = profile.id
                
                return bool(profile_id == obj.profile_id or request.user.is_superuser)
        else:
            return False

    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsSuperUser(BasePermission):
    ''' Allows access only to superusers.'''
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            else:
                return request.user.is_superuser
        else:
            return False

class RegisterUserViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all().order_by('id')
    serializer_class = RegisterSerializer

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
                mixins.ListModelMixin,mixins.RetrieveModelMixin,ProfileWritePermission,viewsets.GenericViewSet): 
    permission_classes = [ProfileWritePermission]
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        '''Mapping profile field to profile of logged in user unless it's superuser editing existing review.'''

        if(self.request.user.is_superuser):
            serializer.save()
        else:
            profile_id = None
            if self.request:
                user_id = self.request.user.id
                profile = Profile.objects.get(user_id=user_id)
                profile_id = profile.id
            serializer.save(profile_id=profile_id)

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
