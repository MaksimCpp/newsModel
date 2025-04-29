from django.db import models
from django.db.models import DateTimeField, ForeignKey, ImageField, TextField
from django.forms import CharField


class News(models.Model):
    title = CharField(max_length=300)
    date = DateTimeField(auto_now_add=True)
    short_text = TextField()
    long_text = TextField()


# Картинки
class NewsImages(models.Model):
    news = ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = ImageField(upload_to='images/')
