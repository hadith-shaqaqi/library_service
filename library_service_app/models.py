from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=120)
    address = models.TextField(blank=True)
    tel = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=120)
    birth_date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="thumbnails", default="thumbnails/default_user.png")


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_year = models.PositiveSmallIntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnails", default="thumbnails/default_book.png")


    def __str__(self):
        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.name
