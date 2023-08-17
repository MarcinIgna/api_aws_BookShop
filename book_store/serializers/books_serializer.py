from rest_framework import serializers
from book_store.models.books_model import Books
from book_store.serializers.genres_serializer import GenreSerializer
from book_store.models.genres_model import Genre


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Books
        fields = ['id', 'title', 'genre', 'description', 'release_year', 'book_isbn', 'author_name', 'author_email']

    def create(self, validated_data):
        genre_data = validated_data.pop('genre', [])
        book = super().create(validated_data)
        for genre in genre_data:
            genre_obj, created = Genre.objects.get_or_create(name=genre['name'])
            book.genre.add(genre_obj)
        return book
    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre', [])
        instance = super().update(instance, validated_data)
        instance.genre.clear()
        for genre in genre_data:
            genre_obj, created = Genre.objects.get_or_create(name=genre['name'])
            instance.genre.add(genre_obj)
        return instance