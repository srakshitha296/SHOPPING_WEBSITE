from django.contrib import admin
from .models import category, product, customer, order

admin.site.register(category)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
