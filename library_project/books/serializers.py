from rest_framework import serializers
from .models import Book


from rest_framework import serializers

from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
