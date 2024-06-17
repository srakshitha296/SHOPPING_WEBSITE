from django.contrib import admin
from .models import Brand, Category, Customer, Product, Order

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
