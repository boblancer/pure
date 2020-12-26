from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30, choices=(
            ("M","male"),
            ("F","female")
        ))
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    release = models.DateTimeField()
    in_stock = models.IntegerField()
    associates = models.ManyToManyField(Person, through="AssociatedPerson")
    url = models.CharField(max_length=100)
    genre = models.ManyToManyField("Genre", related_name="books")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)

class BookGenre(models.Model):
    """
    A class that stores Book ids and Person ids
    """
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT, db_column='book_id')
    genre_id = models.ForeignKey(Person, on_delete=models.PROTECT, db_column='genre_id') 


class AssociatedPerson(models.Model):
    """
    A class that stores Book ids and Person ids
    """
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT, db_column='book_id')
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT, db_column='person_id') 
    relation = models.CharField(max_length=30, db_column='relation')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

