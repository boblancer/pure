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
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.IntegerField()

class AssociatedPerson(models.Model):
    """
    A class that stores Book ids and Person ids
    """
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT, db_column='book_id')
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT, db_column='person_id') 
    relation = models.CharField(max_length=30, db_column='relation')
    timestamp = models.DateTimeField(default=timezone.now, db_column='updated_at')