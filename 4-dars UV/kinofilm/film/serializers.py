from django.urls import include
from rest_framework import serializers
from .models import Category, Movie, Comment



class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Category(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

# ---------------------------------------------------------------------------------

class MovieSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length=0)
    description = serializers.CharField()
    release_date = serializers.DateTimeField()
    made = serializers.CharField(max_length=50)
    language = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Movie(**validated_data)

    def update(self, instance, validated_data):
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.made = validated_data.get('made', instance.made)
        instance.language = validated_data.get('language', instance.language)

# ---------------------------------------------------------------------------------

class CommentSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    author_name = serializers.CharField(max_length=50)
    description = serializers.CharField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.movie_id = validated_data.get('movie_id', instance.movie_id)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


