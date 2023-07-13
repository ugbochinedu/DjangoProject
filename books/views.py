from django.http import HttpResponse
from django.shortcuts import render
from .models import Author

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


# Create your views here.
def welcome(request):
    query_set = Author.objects.get(id=1)
    return render(request, 'books/welcome.html', {"authors": list(query_set)})


def hello(request):
    return HttpResponse("Welcome to semicolon library..")


def get_books(request):
    return HttpResponse("list of books..")