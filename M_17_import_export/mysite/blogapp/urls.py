from django.urls import path
from .views import ArticlesListView, ArticelDetailView, LatestArticlesFeed
app_name='blogapp'

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name="articles"),
    path('articles/<int:pk>/', ArticelDetailView.as_view(), name='article'),
    path('articles/latest/feed/', LatestArticlesFeed(), name='articles-feed'),
]