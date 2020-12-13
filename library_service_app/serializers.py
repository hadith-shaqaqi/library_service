from rest_framework import relations, serializers

from .models import Author, Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ['url', 'name', 'address', 'tel']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['url', 'name', 'birth_date', 'thumbnail']


class BookSerializer(serializers.ModelSerializer):
    # url = relations.HyperlinkedIdentityField(view_name='book', lookup_field='id')

    class Meta:
        model = Book
        fields = ['url', 'title', 'publisher', 'publish_year', 'author', 'thumbnail']


class BookDetailsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['title', 'publisher', 'publish_year', 'author', 'thumbnail']

