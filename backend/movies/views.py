from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserMeSerializer, RegisterSerializer, DirectorSerializer, GenreSerializer, MovieSerializer, MovieListSerializer
from .models import Director, Genre, Movie
from .permissions import IsAdminUserOrReadOnly


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Користувача успішно зареєстровано"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        refresh_token = response.data["refresh"]

        response.set_cookie(
            "refresh_token",
            refresh_token,
            max_age=7 * 24 * 60 * 60,
            httponly=True,
            secure=True,
            samesite="Lax",


            path="/api/token/"
        )
        del response.data["refresh"]

        return response


class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token is None:
            return Response({"detail": "Refresh-токен не надано"}, status=401)

        request.data["refresh"] = refresh_token
        response = super().post(request, *args, **kwargs)

        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"message": "Вихід із системи"})
        response.delete_cookie("refresh_token", path="/api/token/")
        return response


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserMeSerializer(request.user).data)


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related('genre', 'director').all()
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'director', 'year']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'year', 'created_at']
    ordering = ['-year', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        return MovieSerializer
