from functools import wraps
from django.utils import timezone
from .models import Article

def update_last_viewed(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        article = Article.objects.get(pk=kwargs['article_id'])
        article.last_viewed = timezone.now()
        article.last_viewer = request.user.username if request.user.is_authenticated else 'Anonymous'
        article.save()
        return response
    return wrapper
