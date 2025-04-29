from django.urls import path

<<<<<<< HEAD
from news.views import NewsDetail, NewsList
=======
from .views import NewsDetail, NewsList
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e

urlpatterns = [
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
]
