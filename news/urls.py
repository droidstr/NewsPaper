from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostSearch, NewsCreate, NewsEdit, NewsDelete, ArticleCreate, ArticleEdit, ArticleDelete


urlpatterns = [
    path('news/', PostsList.as_view()),
    path('news/<int:pk>', PostDetail.as_view()),
    path('news/search/', PostSearch.as_view()),
    path('news/create/', NewsCreate.as_view()),
    path('news/<int:pk>/edit/', NewsEdit.as_view()),
    path('news/<int:pk>/delete/', NewsDelete.as_view()),
    path('article/create/', ArticleCreate.as_view()),
    path('article/<int:pk>/edit/', ArticleEdit.as_view()),
    path('article/<int:pk>/delete/', ArticleDelete.as_view()),
]
