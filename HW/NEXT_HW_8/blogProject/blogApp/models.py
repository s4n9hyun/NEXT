from django.db import models

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
    def __str__(self):
        return self.title