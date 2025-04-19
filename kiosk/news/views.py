from rest_framework import generics
from .serializers import NewsImagesSerializer
from .models import News, NewsImages


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsImagesSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsImagesSerializer
