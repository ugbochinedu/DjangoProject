from django.http import HttpResponse
from django.shortcuts import render

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


# Create your views here.
def welcome(request):
    return render(request, 'books/welcome.html', {"students": list(users)})


def hello(request):
    return HttpResponse("Welcome to semicolon library..")


def get_books(request):
    return HttpResponse("list of books..")