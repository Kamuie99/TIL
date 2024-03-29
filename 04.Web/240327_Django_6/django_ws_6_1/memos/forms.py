from django import forms
from .models import Memo

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Memo
    fields = '__all__'
  summary = forms.CharField(
    max_length=20,
    widget=forms.TextInput(
      attrs = {
        'placeholder' : 'summary'
      }
    ),
  )
  memo = forms.CharField(
    widget=forms.Textarea(
      attrs = {
        'placeholder' : 'memo',
        'rows' : 5,
        'cols' : 50,
      }
    ),
  )