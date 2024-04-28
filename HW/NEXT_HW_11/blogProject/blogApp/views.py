from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .decorators import update_last_viewed
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
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

@update_last_viewed
def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.filter(parent__isnull=True)

    if request.method == 'POST':
        content = request.POST.get('content')
        nickname = request.POST.get('nickname', 'Anonymous')  # Default to 'Anonymous' if not provided
        parent_id = request.POST.get('parent_id')

        if parent_id:
            # Safely attempt to fetch the parent comment
            parent_comment = get_object_or_404(Comment, id=parent_id)
            new_comment = Comment.objects.create(
                article=article,
                content=content,
                author=nickname,
                parent=parent_comment
            )
        else:
            # If there's no parent_id, we're adding a top-level comment
            new_comment = Comment.objects.create(
                article=article,
                content=content,
                author=nickname
            )

        return redirect('detail', article_id=article_id)

    return render(request, 'detail.html', {'article': article, 'comments': comments})
def list(request):
    articles = Article.objects.all()
    categories = Article.CATEGORY_CHOICES
    category_counts = {cat[0]: Article.objects.filter(category=cat[0]).count() for cat in categories}
    return render(request, 'list.html', {'articles': articles, 'category_counts': category_counts})

def list_by_category(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, 'list.html', {'articles': articles})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
