from rest_framework import viewsets
from .models import Category, Product, Commentary
from .serializer import CategorySerializer, ProductSerializer,CommentarySerializer
from rest_framework.permissions import DjangoModelPermissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    permission_classes = [DjangoModelPermissions]

