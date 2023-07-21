from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


# Create your views here.
@api_view()
def book_list(request):
    return Response('Ok')


@api_view()
def book_details(request, pk):
    return Response(pk)
