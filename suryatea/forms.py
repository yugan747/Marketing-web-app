from dataclasses import fields
from django import forms

from .models import Customer,Order,money_transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model = User 
        fields=['username','email','password1','password2']
class customerform(forms.ModelForm):
    class Meta:
        model=Customer 
        fields =  '__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-style'}),
            'Location':forms.TextInput(attrs={'class':'form-style'}),
            'Contact1':forms.TextInput(attrs={'class':'form-style'}),
            'Contact2':forms.TextInput(attrs={'class':'form-style'}),
            'Customer_Type':forms.Select(attrs={'class':'form-style'}),
           
            'Price':forms.TextInput(attrs={'class':'form-style'}),
            'Note':forms.Textarea(attrs={'class':'form-style'})
            
            
            
            
        }
        
class NewOrderForm(forms.ModelForm):
    class Meta:
        model =Order 
        fields =  ['user','customer','Quantity','ToVisit_date','Price','rating','Product','District']


class moneyform(forms.ModelForm):
    class Meta:
        model= money_transaction   
        fields =   '__all__'   