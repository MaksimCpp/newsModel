from django.db import models
from django.db.models import DateTimeField, ForeignKey, ImageField, TextField
from django.forms import CharField


class News(models.Model):
    title = CharField(max_length=300)
    date = DateTimeField(auto_now_add=True)
    short_text = TextField()
    long_text = TextField()


class NewsImages(models.Model):
    news = ForeignKey(News, on_delete=models.CASCADE)
    image = ImageField(upload_to='images/')
