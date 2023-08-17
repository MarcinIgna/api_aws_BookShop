from django.db import models




class Books(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ManyToManyField("Genre", related_name="books")
    book_isbn = models.CharField(max_length=255, default="0000000000000")
    author_name = models.CharField(max_length=255, default="Unknown")
    author_email = models.EmailField(max_length=255, default="Unknown@o2.pl")
    description = models.TextField()
    release_year = models.IntegerField()
    
    
