from rest_framework.views import APIView
from rest_framework.response import Response
from book_store.models.genres_model import Genre
from book_store.serializers.genres_serializer import GenreSerializer


class GenresView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        else:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)
            
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def put(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response("Genre Deleted")