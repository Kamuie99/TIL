from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Memo

# Create your views here.
def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('memos:index')
  # get 일 때,
  else:
    form = ArticleForm()
  context = {
    'form' : form,
  }
  return render(request, 'memos/create.html', context)

def index(request):
  memos = Memo.objects.all()
  context = {
    'memos' : memos,
  }
  return render(request, 'memos/index.html', context)

def detail(request, memo_pk):
  memos = Memo.objects.get(pk=memo_pk)
  context = {
    'memos' : memos,
  }
  return render(request, 'memos/detail.html', context)

def delete(request, memo_pk):
  memos = Memo.objects.get(pk=memo_pk)
  memos.delete()
  return redirect('memos:index')