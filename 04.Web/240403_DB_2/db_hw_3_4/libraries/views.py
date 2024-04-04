from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect('detail', author_pk=author_pk)
    else:
        form = BookForm()
    context = {
        'author' : author,
        'books' : books,
        'form' : form
    }
    return render(request, 'libraries/detail.html', context)