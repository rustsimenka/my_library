from django.core.validators import MinLengthValidator
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'author']

    title = serializers.CharField(validators=[MinLengthValidator(4)])


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'surname']

