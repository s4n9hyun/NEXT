from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        
        new_article=Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']
        )
        return redirect('list')
    return render(request, 'new.html')


def detail(request, article_id):
    article=Article.objects.get(pk = article_id) # id instead pk is ok
    return render(request, 'detail.html', {'article':article})

def list(request):
    articles = Article.objects.all()
    categories = Article.CATEGORY_CHOICES
    category_counts = {cat[0]: Article.objects.filter(category=cat[0]).count() for cat in categories}
    return render(request, 'list.html', {'articles': articles, 'category_counts': category_counts})

def list_by_category(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, 'list.html', {'articles': articles})
