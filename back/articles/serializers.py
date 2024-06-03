from rest_framework import serializers
from .models import Category, Article, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('pk','title', 'category', )


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    article = ArticleListSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        