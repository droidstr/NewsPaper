from django.urls import path
# Импортируем созданное нами представление
from .views import UserEdit, become_an_author


urlpatterns = [
    path('<int:pk>/edit/', UserEdit.as_view()),
    path('upgrade/', become_an_author, name='upgrade')
]
