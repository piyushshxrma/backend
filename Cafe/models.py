from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


class Table(models.Model):
    number = models.IntegerField()
    is_available = models.BooleanField()
    def __str__(self):
        return str(self.number)

class Order(models.Model):
    
    PENDING = 'P'
    CONFIRMED = 'C'
    CANCELLED = 'X'
    CASH = 'C'
    CARD = 'D'
    ONLINE = 'O'
    STATUS_CHOICES = {
       PENDING : 'Pending',
       CONFIRMED : 'Confirmed',
       CANCELLED : 'Cancelled',
    }
    PAYMENT_CHOICES = {
        CASH : 'Cash',
        CARD : 'Card',
        ONLINE : 'Online',
        
    }
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    table = models.ForeignKey(Table,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=1,choices = STATUS_CHOICES, default = PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100,choices = PAYMENT_CHOICES, default = CASH)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Related order
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Auto-fill from Product

    

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.order}"