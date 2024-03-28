from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('check/', views.check, name='check'),
]
