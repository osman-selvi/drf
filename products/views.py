from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from . import models
from . import serializers

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class AboutViewSet(ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer