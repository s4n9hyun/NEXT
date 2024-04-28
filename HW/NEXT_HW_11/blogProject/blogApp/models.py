from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    CATEGORY_CHOICES = [
        ('취미', '취미'),
        ('프로그래밍', '프로그래밍'), 
        ('음식', '음식'),
    ]
    title=models.CharField(max_length=200)
    content=models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='취미')
    created_at = models.DateTimeField(auto_now_add=True)
    last_viewed = models.DateTimeField(auto_now=True)
    last_viewer = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', kwargs={'article_id': self.id})

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # This field is for nested comments
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.author} - {self.content}'

    # Property to differentiate between a comment and a reply
    @property
    def is_reply(self):
        return self.parent is not None