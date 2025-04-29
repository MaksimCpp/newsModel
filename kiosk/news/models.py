from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    short_text = models.TextField()
    long_text = models.TextField()


# Картинки
class NewsImages(models.Model):
<<<<<<< HEAD
    news = ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = ImageField(upload_to='images/')
=======
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e
