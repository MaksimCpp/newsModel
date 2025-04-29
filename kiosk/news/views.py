from rest_framework import generics

<<<<<<< HEAD
from news.models import News
from news.serializers import NewsSerializer
=======
from .models import News
from .serializers import NewsImagesSerializer
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
<<<<<<< HEAD
    serializer_class = NewsSerializer
=======
    serializer_class = NewsImagesSerializer
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
<<<<<<< HEAD
    serializer_class = NewsSerializer
=======
    serializer_class = NewsImagesSerializer
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e
