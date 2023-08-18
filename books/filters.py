from django_filters import FilterSet

from books.models import Book


class CustomFilter(FilterSet):

    class Meta:
        model = Book
        fields = {
            'author_id': ['exact'],
            'title': ['exact'],
            'copies': ['gt','lt']
        }