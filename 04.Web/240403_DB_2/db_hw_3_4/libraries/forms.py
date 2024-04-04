from django import forms
from .models import Book

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    # fields = '__all__'  # 이따 생각 다시해보자
    exclude = ['author']