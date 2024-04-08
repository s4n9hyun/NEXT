from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title

    @property
    def d_day(self):
        return (self.deadline - now().date()).days
