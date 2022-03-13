from django.contrib import admin
from .models import Customer,Order,money_transaction
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(money_transaction)



