from rest_framework.viewsets import ModelViewSet

from library.models import Book, Author
from library.serialiser import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
