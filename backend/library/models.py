from django.db import models


class ExplicitModel(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager()


class Author(ExplicitModel):
    first_name = models.CharField(max_length=64, null=False)
    surname = models.CharField(max_length=64, null=False)


class Book(ExplicitModel):
    title = models.CharField(max_length=256, min_lengt=4, null=False, unique=True)
    pages = models.IntegerField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    amount_books = models.IntegerField(null=True, blank=False, default=0)

    def count_amount_of_readers(self):
        pass

    def count_books_left(self):
        pass


class Reader(Author):
    now_reading = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    books_read = models.ManyToManyField(Book, related_name='readers', blank=True)


def get_count_books_read_before(self):
    pass
