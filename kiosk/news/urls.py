from django.urls import path

from .views import NewsDetail, NewsList

urlpatterns = [
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
]
