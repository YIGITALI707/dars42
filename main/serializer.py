from rest_framework import serializers
from .models import Category,Commentary,Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Commentary
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
