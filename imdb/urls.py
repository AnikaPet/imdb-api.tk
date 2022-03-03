from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

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
    path('',views.about_us,name='home-page'),

    path('documents/',views.documents),
    path('documents/actor/',views.actor_docs),
    path('documents/cast/',views.cast_docs),
    path('documents/company/',views.company_docs),
    path('documents/country/',views.country_docs),
    path('documents/language/',views.language_docs),
    path('documents/movie/',views.movie_docs),
    path('documents/review/',views.review_docs),
    path('documents/profile/',views.profile_docs),
    path('documents/token/',views.token_docs),
    path('documents/image/',views.image_docs),
    path('documents/genre/',views.genre_docs),

    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    #enable login
    #path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework')),

    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/image/movie/<int:movie_id>',views.movie_image_view),
    path('api/image/actor/<int:actor_id>',views.actor_image_view),

]

'''    path('docs/',include_docs_urls(title='IMDB-api')),
    path('schema', get_schema_view(
        title="IMDB API",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
'''