from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    CookieTokenObtainPairView,
    CookieTokenRefreshView,
    LogoutView,
    MeView,
    DirectorViewSet,
    GenreViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="api_logout"),
    path("me/", MeView.as_view(), name="api_me"),
    path("", include(router.urls)),
]