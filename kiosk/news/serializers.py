from rest_framework import serializers

<<<<<<< HEAD
from news.models import News, NewsImages
=======
from .models import News, NewsImages
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('id', 'image')


class NewsSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = '__all__'

    def create(self, validated_data):
        images = self.context.get('request').FILES.getlist('images') # DeepSeek
        news = News.objects.create(**validated_data)

        for image in images:
            NewsImages.objects.create(news=news, image=image)

        return news
    
    def update(self, instance, validated_data):
        images = self.context.get('request').FILES.getlist('images') # DeepSeek
        instance.title = validated_data.get('title', instance.title)
        instance.short_text = validated_data.get('short_text', instance.short_text)
        instance.long_text = validated_data.get('long_text', instance.long_text)

        for image in images:
            NewsImages.objects.create(news=instance, image=image)

        return instance
=======
    class Meta:
        model = News
        fields = ('id', 'title', 'date', 'short_text', 'long_text', 'images')


class NewsImagesSerializer(NewsSerializer):
    images = ImagesSerializer(many=True, required=False)
>>>>>>> 52eaa2a3857b3d4e29f6d169cd6b6f4d00287f7e
