from django.shortcuts import redirect, render,HttpResponse

from .forms import customerform,NewOrderForm, moneyform,createuserform
from .models import Choices4, Customer,Order,money_transaction
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.info(request,'Username or Password is Incorrect') 
            return render(request,'login.html')   
   
    return render(request,'login.html')

def register(request):
    form = createuserform()
    if request.method=='POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Acount was created for'+user)
            return redirect('loginPage')
    context={'form':form}
    
    return render(request,'register1.html',context) 


def logoutPage(request):
    logout(request)   
    return redirect('loginPage')    



@permission_required('Surya.add_customer',login_url='loginPage')
def home(request):
    return render(request,'home.html')

def register1(request):
    form =customerform(initial={'user':request.user})
    if request.method=="POST":
        form = customerform(request.POST , request.FILES)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect(neworder)
          


    context={'form':form}  
    return render(request,'register.html',context)    

def neworder(request):
    
    
    form = NewOrderForm(initial={'user':request.user})
    if request.method=="POST":
        form = NewOrderForm(request.POST , request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect(sucess)


            



            

    context={'form':form}  
    return render(request,'neworder.html',context)    


def sucess (request):
    return render(request,'sucess.html')


def Kathmandu_alert(request):
    
    order=Order.objects.filter(user=request.user,ToVisit_date=datetime.date.today(),Visited = False,District='1').order_by('-rating')|Order.objects.filter(user=request.user,Hold = True)

    context={'alert_order':order}
    
   

    print(request.user)
    


       
       
       

   
    

    return render(request,'alert_kathmandu.html',context)

def Lalitpur_alert(request):
    
    order=Order.objects.filter(user=request.user,ToVisit_date=datetime.date.today(),Visited = False,District='2').order_by('-rating')|Order.objects.filter(user=request.user,Hold = True)

    context={'alert_order':order}
    
   

    print(request.user)
    


       
       
       

   
    

    return render(request,'alert_Lalitpur.html',context)


def Bhaktapur_alert(request):
    
    order=Order.objects.filter(user=request.user,ToVisit_date=datetime.date.today(),Visited = False,District='3').order_by('-rating')|Order.objects.filter(user=request.user,Hold = True)

    context={'alert_order':order}
    
   

    print(request.user)
    


       
       
       

   
    

    return render(request,'alert_Bhaktapur.html',context)


def cash(request,id):
    order =Order.objects.get(id=id)
   
    print(order)
    form = moneyform(initial={'order':order})
    if request.method=="POST":
        form = moneyform(request.POST)
        if form.is_valid():
            form.save()
            order.Visited=True
            order.save() 
   
            return redirect(salescash)

    context={'form':form}       
    return render(request,'cashsubmission.html',context) 


  
def customer_details(request):
    
    return render(request,'customer_details.html')

def salescash(request):
    return render(request,'salescash.html')
   
   
def mysales(request):
    order = Order.objects.filter(user=request.user,Visited=True,ToVisit_date=datetime.date.today())
    context={'order':order}
    return render(request,'cashsales.html',context)
    


    


    

def kathmandu_details(request):
    if request.method == 'POST':
        search=request.POST['searchcustomer']
        customer =Customer.objects.filter(Name=search,user=request.user,District='1')
        print(customer)
        context={'customer':customer}
        

        return render(request,'searchcustomer.html',context)
    customer =Customer.objects.filter(user=request.user,District='1')    
    context={'customer':customer}

    return render(request,'ktm_details.html',context)
def bhaktapur_details(request):
    if request.method == 'POST':
        search=request.POST['searchcustomer']
        customer =Customer.objects.filter(Name=search,user=request.user,District='3')
        print(customer)
        context={'customer':customer}


        return render(request,'searchcustomer.html',context)
    customer =Customer.objects.filter(user=request.user,District='3')    
    context={'customer':customer}

    return render(request,'Bkt_details.html',context)

def lalitpur_details(request):
    if request.method == 'POST':
        search=request.POST['searchcustomer']
        customer =Customer.objects.filter(Name=search,user=request.user,District='2')
        print(customer)
        context={'customer':customer}


        return render(request,'searchcustomer.html',context)
    customer =Customer.objects.filter(user=request.user,District='2')  
      
    context={'customer':customer}

    return render(request,'ltp_details.html',context)        

def customer_transactions(request):
    if request.method == 'POST':
        search=request.POST['searchname']
        customer =Customer.objects.filter(Name=search)
        context={'customer':customer}
        

        return render(request,'customer_transactions2.html',context)
       
       
      

   
    
 

    customer =Customer.objects.filter(user=request.user)
    context={'customer':customer}
    return render(request,'customer_transactions.html',context)

def showtransactions(request,id): 

    order=Customer.objects.filter(user=request.user,id=id)

    
    

    


    print(order)
    
    context={'order':order}
    return render(request,'showtransactions.html',context)

def customeralert_details(request,id):
    customer = Customer.objects.filter(id=id)
    context={'cus':customer}
    return render(request,'customeralert_details.html',context)
def ktm_details(request,id):
    
    customer = Customer.objects.filter(user=request.user,id=id)
    context ={'customer':customer }
    return render(request,'ktminner_details.html',context)

def bkt_details(request,id):
    customer = Customer.objects.filter(user=request.user,id=id)
    context ={'customer':customer }
    return render(request,'bktinner_details.html',context)  

def ltp_details(request,id):
    customer = Customer.objects.filter(user=request.user,id=id)
    context ={'customer':customer }
    return render(request,'ltpinner_details.html',context)  



def showcustomer(request,id):
    customer=Customer.objects.filter(user=request.user,id=id) 
    context={'customer':customer}
    return render(request,'showcustomer.html',context)   

def Delete_kathmandu(request,id):
    order =Order.objects.filter(user = request.user,id=id)
    order.delete()
    return redirect(Kathmandu_alert)
    
def update_kathmandu(request,id):
    order =Order.objects.get(id=id)
    form = NewOrderForm(request.POST or None,instance=order)
    if form.is_valid():
        form.save()
        return redirect(Kathmandu_alert)

    context={'form':form}    


    return render(request,'update_alert.html',context)    
def Delete_lalitpur(request,id):
    order =Order.objects.filter(user = request.user,id=id)
    order.delete()
    return redirect(Lalitpur_alert)
    
def update_lalitpur(request,id):
    order =Order.objects.get(id=id)
    form = NewOrderForm(request.POST or None,instance=order)
    if form.is_valid():
        form.save()
        return redirect(Lalitpur_alert)

    context={'form':form}    


    return render(request,'update_alert.html',context)    

def Delete_bhaktapur(request,id):
    order =Order.objects.filter(user = request.user,id=id)
    order.delete()
    return redirect(Bhaktapur_alert)
    
def update_bhaktapur(request,id):
    order =Order.objects.get(id=id)
    form = NewOrderForm(request.POST or None,instance=order)
    if form.is_valid():
        form.save()
        return redirect(Bhaktapur_alert)

    context={'form':form}    


    return render(request,'update_alert.html',context)        


def alert(request):
    return render(request,'alert_district.html')