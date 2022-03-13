from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now




Choices1 =(
    ('HT','Hotel'),
    ('Kr','Kirana'),
    ('HM','Home'),
    ('OT','Others'),
)

Choices3 =(
    ('1','Kathmandu'),
     ('2','Lalitpur'),
    ('3','Bhaktapur')
   
    
)
Choices4 =(
    ('3','Good'),
    ('2','Average'),
    ('1','Poor'),
    ('0','cash')
    
)






class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=120,null=True,blank=True,unique=True)
    Route = models.CharField(max_length=120,null=True,blank=True)
    District=models.CharField(max_length=200,choices=Choices3,blank=True)
  
    location = models.CharField(max_length=200)
    Contact1 = models.PositiveIntegerField( null = True, blank = True)
    Contact2= models.PositiveIntegerField( null = True, blank = True)
    Customer_type=models.CharField(max_length=200,choices=Choices1)
   
    AveragePrice=models.PositiveIntegerField(default=400)
    Note = models.TextField(null=True,blank=True)
    
    Image = models.ImageField(upload_to='media/pictures',blank=True)
    Images_Map = models.ImageField(upload_to='media/pictures',blank=True)

   
   


    def __str__(self):
        return self.Name


class Order(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Quantity=models.PositiveIntegerField(null=True)
    Price=models.PositiveIntegerField(default=400)
    Ordered_date=models.DateTimeField(auto_now_add=True)
    District=models.CharField(max_length=200,choices=Choices3,blank=True)
    
    ToVisit_date = models.DateField(null=True)
    Visited = models.BooleanField(default = False)
    rating = models.CharField(max_length=120,choices=Choices4)
    Product=models.CharField(max_length=200,blank=True)
    
    Hold = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.customer)

    @property
    def total_cash(self):
        total = self.Quantity*self.Price
        return total

  




 





class money_transaction(models.Model):
    order = models.OneToOneField(Order,on_delete=models.SET_NULL,null=True)  
    cash = models.PositiveIntegerField(null=True) 
    Date = models.DateTimeField(default=now, editable=False)
   
    def __str__(self):
        return str(self.order)


    @property
    def remain_credit(self):
        remaining_credit = self.order.total_cash-self.cash
        return remaining_credit



   


  




    


