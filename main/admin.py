from django.contrib import admin
from .models import Category,Product,Commentary
# Register your models here.


admin.site.register(Commentary)
admin.site.register(Category)
admin.site.register(Product)
