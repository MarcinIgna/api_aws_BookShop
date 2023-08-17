from rest_framework.views import APIView
from rest_framework.response import Response
from book_store.models.books_model import Books
from book_store.serializers.books_serializer import BookSerializer


class BooksView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            book = Books.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            books = Books.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def put(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self, request,pk):
        book = Books.objects.get(pk=pk)
        book.delete()
        return Response("Book Deleted")