from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'articles/index.html', context)

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
      article = form.save()
      return redirect('my_app:check')
  else:
    form = ArticleForm()
  context = {
    'form' : form,
  }
  return render(request, 'articles/create.html', context)

def check(request):
  return render(request, 'articles/check.html')
    