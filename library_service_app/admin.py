from django.contrib import admin

from .forms import AuthorForm, BookForm, PublisherForm
from .models import Author, Book, Publisher


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    form = PublisherForm

admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    form = AuthorForm

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    raw_id_fields = ['publisher', 'author']
    form = BookForm

admin.site.register(Book, BookAdmin)
