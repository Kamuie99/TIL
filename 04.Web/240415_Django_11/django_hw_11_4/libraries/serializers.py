from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'
        
    def get_reviews(self, obj):
        reviews = obj.review_set.all().values('content', 'score')
        return list(reviews)

class ReviewListSerializer(serializers.ModelSerializer):
    book_isbn = serializers.CharField(source='book.isbn', read_only=True)
    
    class Meta:
        model = Review
        fields = ('content', 'score', 'book_isbn',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)