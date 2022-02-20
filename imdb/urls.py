from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
router.register(r'register',views.RegisterUserViewSet)

urlpatterns = [
    #path('',),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    #enable login
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
