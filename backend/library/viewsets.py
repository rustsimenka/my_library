
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Author
from library.serialiser import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get'])
    def get_name_book(self, request_id, pk=None):
        try:
            book = self.get_object()
            return Response({f'Под id {pk} записана книга: {book.title}'})
        except Book.DoesNotExist:
            return Response({'Книга не найдена'})


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
