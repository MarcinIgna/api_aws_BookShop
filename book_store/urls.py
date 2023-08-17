from django.urls import path
from .views.books_view import BooksView
from .views.genres_view import GenresView

app_name = "book_store"
urlpatterns = [
    path("books/", BooksView.as_view(), name="books"),
    path("books/<int:pk>/", BooksView.as_view(), name="book"),
    path("genres/", GenresView.as_view(), name="genres"),
    path("genres/<int:pk>/", GenresView.as_view(), name="genre"),
]
