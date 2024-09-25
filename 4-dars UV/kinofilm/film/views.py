from http.client import responses

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from unicodedata import category

from .models import Movie, Category, Comment
from .serializers import CategorySerializer, MovieSerializer, CommentSerializer


# Create your views here.


class CategoryListView(APIView):

    def get(self, request: Request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                return Response(CategorySerializer(category).data)
            except:
                return Response({"error": "Does not exist"})

        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)

    def post(self, request: Request, pk=None):
        if not pk:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            category = serializer.save()
            return Response(CategorySerializer(category).data)
        return Response({"error": "Method POST not allowed"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(instance=category, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(CategorySerializer(category).data)
            except:
                return Response({"error": "Does not exist"})
        return Response({"error": "Method PUT not allowed"})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                category.delete()
                return Response({"message": "success"})
            except:
                return Response({"error": "Does not exist"})
        return Response({"error": "Method DELETE not allowed"})


# ---------------------------------------------------------------------

class MovieListView(APIView):

    def get(self, request: Request, pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk)
                return Response(MovieSerializer(movie).data)
            except:
                return Response({"error": "Does not exist"})

        movies = Movie.objects.all()
        return Response(MovieSerializer(movies, many=True).data)

    def post(self, request: Request, pk=None):
        if not pk:
            serializer = MovieSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            movie = serializer.save()
            return Response(MovieSerializer(movie).data)
        return Response({"error": "Method POST not allowed"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(instance=movie, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(MovieSerializer(movie).data)
            except:
                return Response({"error": "Does not exist"})
        return Response({"error": "Method PUT not allowed"})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk)
                movie.delete()
                return Response({"message": "success"})
            except:
                return Response({"error": "Does not exist"})
        return Response({"error": "Method DELETE not allowed"})


# ---------------------------------------------------------------------

class CommentListView(APIView):

    def get(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                return Response(CommentSerializer(comment).data)
            except:
                return Response({"error": "Does not exist"})

        comments = Comment.objects.all()
        return Response(CommentSerializer(comments, many=True).data)

    def post(self, request: Request, pk=None):
        if not pk:
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            comment = serializer.save()
            return Response(CommentSerializer(comment).data)
        return Response({"error": "Method POST not allowed for a specific ID"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(instance=comment, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(CommentSerializer(comment).data)
            except:
                return Response({"error": "Does not exist"})
        return Response({"error": "Method PUT not allowed"})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                comment.delete()
                return Response({"message": "success"})
            except:
                return Response({"error": "Does not exist"})
        return Response({"error": "Method DELETE not allowed"})
