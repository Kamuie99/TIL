from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = Review.objects.filter(book=book)
    review_form = ReviewForm()
    context = {
        'book': book,
        'reviews': reviews,
        'review_form': review_form,
        'book_pk' : book_pk,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def reviews_create(request, pk):
    book = Book.objects.get(pk=pk)
    review_form = ReviewForm(request.POST)
    reviews = book.review_set.all()
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = request.user
        review.book = book
        review_form.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'book' : book,
        'review_form' : review_form,
        'reviews' : reviews, 
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def reviews_delete(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('libraries:detail', book_pk)