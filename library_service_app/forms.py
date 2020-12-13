from django import forms

from .models import Author, Book, Publisher


class PublisherForm(forms.ModelForm):
    """Input form for publisher."""
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'tel']


class AuthorForm(forms.ModelForm):
    """Input form for publisher."""
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'thumbnail']


class BookForm(forms.ModelForm):
    """Input form for publisher."""
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'publish_year', 'author', 'thumbnail']
