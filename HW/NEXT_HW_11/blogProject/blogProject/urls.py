from django.contrib import admin
from django.urls import path
from blogApp import views
from blogApp.views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('detail/<int:article_id>',views.detail, name='detail'),
    path('category/<str:category>', views.list_by_category, name='list_by_category'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
