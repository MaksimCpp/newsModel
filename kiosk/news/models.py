from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    short_text = models.TextField()
    long_text = models.TextField()


# Картинки
class NewsImages(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

