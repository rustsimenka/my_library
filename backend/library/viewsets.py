from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Book, Author
from .serialiser import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get'])
    def get_name_book(self, request, pk=None):
        try:
            book = self.get_object()
            return Response({f'Под id {pk} записана книга: {book.title}'})
        except Http404:
            return Response({'Книга не найдена'}, status=404)

    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('title', openapi.IN_QUERY, description="Название книги",
                          type=openapi.TYPE_STRING, required=False)])
    @action(detail=False, methods=['get'])
    def get_filter_name_book(self, request, pk=None):
        title = request.query_params.get('title')

        books = Book.objects.filter(title=title)
        response_data = []

        for book in books:
            response_data.append({'message': f'С названием "{book.title}" есть книга автора {book.author.first_name}'
                                             f' {book.author.surname}.'})
        if not response_data:
            return Response({'error': 'Книги с таким названием не найдены'}, status=404)
        return Response(response_data)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @swagger_auto_schema(method='get', manual_parameters=[
        openapi.Parameter('first_name', openapi.IN_QUERY, description="Имя автора",
                          type=openapi.TYPE_STRING, required=False),
        openapi.Parameter('surname', openapi.IN_QUERY, description="Фамилия автора",
                          type=openapi.TYPE_STRING, required=False, default='')
    ])
    @action(detail=False, methods=['get'])
    def get_authors_books(self, request):
        first_name = request.query_params.get('first_name')
        surname = request.query_params.get('surname')

        try:
            books = Book.objects.filter(author__first_name=first_name, author__surname=surname)
            book_titles = [book.title for book in books]
            return Response({f'От автора {first_name} {surname} есть книги': book_titles})
        except Http404:
            return Response({'Автор не найден'}, status=404)
