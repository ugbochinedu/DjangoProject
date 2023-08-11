from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, ReviewModel, BookInstance
from .serializers import AuthorSerializer, CreateBooKSerializer, BooKSerializer, CreateAuthorSerializer, \
    ReviewSerializer, BookInstanceSerializer

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooKSerializer

    # def destory(self, request, *args, **kwargs):

    def get_serializer_context(self):
        return {'request': self.request}


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return ReviewModel.objects.filter(book_id=self.kwargs['book_pk'])


class BookInstanceViewSet(ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer

    def get_serializer_context(self):
        return BookInstance.objects.filter(book_id=self.kwargs['book_pk'])

# class BookList(ListCreateAPIView):
# queryset = Book.objects.all()
# serializer_class = CreateBooKSerializer
#
# def get_serializer_context(self):
#     return {'request': self.request}
# def get_queryset(self):
#     return Book.objects.all()
#
# def get_serializer_class(self):
#     return BooKSerializer

# def get(self, request):
#     queryset = Book.objects.all()
#     serializer = BooKSerializer(queryset, many=True, context={'request': request})
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def post(self, request):
#     serializer = CreateBooKSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooKSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.response}


# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BooKSerializer(book, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = CreateBooKSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = CreateAuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = CreateAuthorSerializer

# class AuthorList(APIView):
#     def get(self, request):
#         query_set = Author.objects.all()
#         serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AuthorDetail(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('author').all()
#         serializer = BooKSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateBooKSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BooKSerializer(book, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = CreateBooKSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         query_set = Author.objects.all()
#         serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     if request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
