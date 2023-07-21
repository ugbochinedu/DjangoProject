from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    isbn = serializers.CharField(max_length=13)
    genre = serializers.CharField(max_length=8)