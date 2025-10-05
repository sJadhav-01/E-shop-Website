from django.db import models
from .customer import Customer
from .product import Product
# import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.CharField(max_length=13)
    address = models.TextField(max_length=100, null=True, blank=True) 
    # date = models.DateTimeField(default=datetime.datetime.today)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    
        # auto_now vs. auto_now_add
        # auto_now - Use Case - Records the last modification time. Ideal for a last_updated or modified_at field.	Updates every time Model.save() is called.
        # auto_now_add - Use Case - Records the creation time. Perfect for a created_at or date_joined field. Only sets the value on the initial creation of the object.

    
    def place_order(self):
        return self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')