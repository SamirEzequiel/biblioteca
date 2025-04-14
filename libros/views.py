from django.shortcuts import render

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse

from rest_framework import generics
from .models import Libro, Autor, Editor
from .serializers import LibroSerializer, AutorSerializer, EditorSerializer

from rest_framework.response import Response 
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters

# Importaciones para autenticación
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

"""
Este módulo contiene las vistas de la API REST para la gestión de libros, autores y editores.
Implementa endpoints para listar, crear, filtrar y buscar recursos.
"""

class LibroFilter(FilterSet):
    """
    Filtro personalizado para la búsqueda de libros.
    Permite filtrar por título, editor, autores y rango de precios.
    """
    titulo = filters.CharFilter("titulo")
    editor = filters.CharFilter("editor__nombre")
    autores = filters.CharFilter("autores__nombre")
    min_precio = filters.CharFilter(method="filter_by_min_precio")
    max_precio = filters.CharFilter(method="filter_by_max_precio")

    class Meta:
        model = Libro
        fields = ("titulo", "editor", "autores")

    def filter_by_min_precio(self, queryset, name, value):
        """Filtra libros con precio mayor al valor especificado"""
        queryset = queryset.filter(precio__gt=value)
        return queryset

    def filter_by_max_precio(self, queryset, name, value):
        """Filtra libros con precio menor al valor especificado"""
        queryset = queryset.filter(precio__lt=value)
        return queryset

class LibroList(generics.ListCreateAPIView):
    """
    Vista para listar y crear libros.
    Implementa filtrado, ordenamiento y búsqueda.
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    # Autenticación y permisos comentados por defecto
    # authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated, IsAdminUser,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = LibroFilter
    ordering_fields = ("titulo",)
    ordering = ("-titulo")
    search_fields = ("titulo",)

class AutorFilter(FilterSet):
    """
    Filtro personalizado para la búsqueda de autores.
    Permite filtrar por nombre de autor.
    """
    autores = filters.CharFilter(method="filter_by_nombre")

    class Meta:
        model = Autor
        fields = ("id", "nombre",)

    def filter_by_nombre(self, queryset, name, value):
        """Filtra autores por nombre, permitiendo múltiples nombres separados por comas"""
        nombres = value.strip().split(",")
        queryset = queryset.filter(nombre__in=nombres).distinct()
        return queryset

class AutorList(generics.ListCreateAPIView):
    """
    Vista para listar y crear autores.
    Implementa filtrado por nombre.
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AutorFilter

class EditorList(generics.ListCreateAPIView):
    """
    Vista para listar y crear editores.
    """
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

def buscar_libro(request):
    """
    Función de búsqueda simple de libros por título.
    Retorna resultados en formato JSON.
    """
    buscar = "a"  # Valor por defecto para la búsqueda
    libros = Libro.objects.filter(titulo__contains=buscar)
    serializer = LibroSerializer(libros, many=True)
    return JsonResponse(serializer.data, safe=False)

from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    """
    Vista para el inicio de sesión de usuarios.
    Genera un token de autenticación al iniciar sesión.
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)

class LogoutView(APIView):
    """
    Vista para cerrar sesión de usuarios.
    Invalida el token de autenticación.
    """
    authentication_classes = {TokenAuthentication,}

    def post(self, request):
        django_logout(request)
        return Response(status=204)
