from rest_framework import serializers
from .models import Product, Category, About

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'title', 'text', 'image', 'category', 'created_at', 'updated_at')

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title', 'description', 'image')