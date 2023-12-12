from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.AutoField
    product_name = models.CharField(max_length=50)
    category_choices = (
        ('Category', 'Select Category'),
        ('Vegetable', 'Vegetable'),
        ('Fruits', 'Fruits'),
        ('Dry Fruits', 'Dry Fruits'),
        ('Daily Needs', 'Daily Needs'),
        ('Stationary', 'Stationary'),
        ('Medicine', 'Medicine'),
        ('Fashion', 'Fashion'),
        ('Cosmetics', 'Cosmetics'),
        ('Computer & Acces', 'Computer & Acces'),
        ('Electronics', 'Electronics'),
        ('Electricals', 'Electricals'),
        ('Other', 'Other')
    )
    category = models.CharField(max_length=50, default="Category", choices=category_choices)
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    decs = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/product_img", default="")
    
    def __str__(self):
        return self.category + " | " + self.product_name
        
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.user} | {self.quantity} x {self.product.product_name}'
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)    
    email = models.CharField(max_length=70)    
    phone = models.CharField(max_length=14)    
    desc = models.CharField(max_length=700)    
    
    def __str__(self):
        return f"Message form -> {self.name}"
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=14)
    landmark = models.CharField(max_length=70)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    zip_code = models.CharField(max_length=6)

    cart_items = models.JSONField(default=list)
    order_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Order from - {self.name} | {self.phone}"  

class Career(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)    
    email = models.CharField(max_length=70)    
    phone = models.CharField(max_length=13)  
    qual = models.CharField(max_length=70)    
    skill = models.CharField(max_length=70)    
    desc = models.CharField(max_length=500)    
    
    def __str__(self):
        return f"{self.name}'s career inquiry"    