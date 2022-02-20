from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r'profiles', views.ProfileViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'cast', views.CastViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'actors', views.ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #enable login
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework'))
]
