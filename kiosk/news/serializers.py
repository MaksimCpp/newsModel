from rest_framework import serializers


from news.models import News, NewsImages
from news.models import News, NewsImages


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('id', 'image')


class NewsSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = '__all__'

    def create(self, validated_data):
        images = self.context.get('request').FILES.getlist('images')
        news = News.objects.create(**validated_data)

        for image in images:
            NewsImages.objects.create(news=news, image=image)

        return news
    
    def update(self, instance, validated_data):
        images = self.context.get('request').FILES.getlist('images') 
        instance.title = validated_data.get('title', instance.title)
        instance.short_text = validated_data.get('short_text', instance.short_text)
        instance.long_text = validated_data.get('long_text', instance.long_text)

        for image in images:
            NewsImages.objects.create(news=instance, image=image)

        return instance
