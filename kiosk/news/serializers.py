from rest_framework import serializers

from .models import News, NewsImages


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('id', 'image')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'date', 'short_text', 'long_text', 'images')


class NewsImagesSerializer(NewsSerializer):
    images = ImagesSerializer(many=True, required=False)
