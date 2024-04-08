from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    
    # M:N 관계 설정
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles')
    
    def __str__(self):
        return self.title
