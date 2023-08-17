from django.contrib import admin
from .models.books_model import Books
from .models.genres_model import Genre

# Register your models here.
admin.site.register(Books)
admin.site.register(Genre)