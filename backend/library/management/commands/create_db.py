from django.core.management.base import BaseCommand
from library.models import Author, Book, Reader

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        authors_books = [
            ('Лев', 'Толстой', 'Война и мир', 224),
            ('Лев', 'Толстой', 'Анна Каренина', 864),
            ('Фёдор', 'Достоевский', 'Преступление и наказание', 430),
            ('Фёдор', 'Достоевский', 'Идиот', 560),
            ('Анна', 'Ахматова', 'Реквием', 160),
            ('Анна', 'Ахматова', 'Поэмы', 200),
            ('Михаил', 'Булгаков', 'Мастер и Маргарита', 384),
            ('Михаил', 'Булгаков', 'Собачье сердце', 256),
            ('Александр', 'Пушкин', 'Евгений Онегин', 350),
            ('Александр', 'Пушкин', 'Руслан и Людмила', 200),
            ('Иван', 'Тургенев', 'Отцы и дети', 320),
            ('Борис', 'Пастернак', 'Доктор Живаго', 608),
            ('Рэй', 'Брэдбери', '451 градус по Фаренгейту', 256),
            ('Джордж', 'Оруэлл', '1984', 328),
            ('Фрэнсис', 'Скотт Фицджеральд', 'Великий Гэтсби', 180),
        ]

        for first_name, surname, title, pages in authors_books:
            author, created = Author.objects.get_or_create(first_name=first_name, surname=surname)
            Book.objects.create(title=title, pages=pages, author=author)

        readers = [
            ('Анна', 'Смирнова'),
            ('Сергей', 'Иванов'),
            ('Ирина', 'Петрова'),
            ('Алексей', 'Сидоров'),
            ('Мария', 'Кузнецова'),
            ('Дмитрий', 'Васильев'),
            ('Ольга', 'Федорова'),
            ('Павел', 'Михайлов'),
            ('Екатерина', 'Николаева'),
            ('Никита', 'Орлов'),
        ]

        for first_name, surname in readers:
            Reader.objects.create(first_name=first_name, surname=surname)

        self.stdout.write(self.style.SUCCESS('Database populated with more books successfully!'))