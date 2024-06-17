from django.contrib import admin
from .models import categories, products, customers, orders

admin.site.register(categories)
admin.site.register(customers)
admin.site.register(products)
admin.site.register(orders)
