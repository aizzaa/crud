from rest_framework.serializers import ModelSerializer
from .models import Category, Tag, Post


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


