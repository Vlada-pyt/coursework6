from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_image = serializers.ImageField(source='author.image')
    author_id = serializers.ReadOnlyField(source='author.id')
    ad_id = serializers.ReadOnlyField(source='ad.id')

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author_id', 'author_first_name', 'created_at', 'author_last_name', 'author_image', 'ad_id']


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", 'price', 'title', 'image', 'description']


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    phone = serializers.CharField(source="author.phone")

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'phone', 'price', 'author_id', 'author_first_name', 'author_last_name', 'description']
