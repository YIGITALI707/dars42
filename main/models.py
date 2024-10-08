from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name=models.CharField(max_length=50)


    def __str__(self):
        return self.category_name


class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name},{self.description}"


class Commentary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    commentery_for_product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.commentery_for_product}"

