from django.db import models
import datetime

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    emaild = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    
    #Sale
    if_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='',)
    phone = models.CharField(max_length=10, default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

