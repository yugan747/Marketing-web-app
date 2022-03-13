from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/',views.home,name='home'),
    path('register1/',views.register1,name='register1'),
     
   
    path('neworder/',views.neworder,name='neworder'),
    path('sucess/',views.sucess,name='sucess'),
    path('myalert/',views.alert,name='alert'),
    path('Kathmandu_alert/',views.Kathmandu_alert,name='Kathmandu_alert'),
    path('Bhaktapur_alert/',views.Bhaktapur_alert,name='Bhaktapur_alert'),
    path('Lalitpur_alert/',views.Lalitpur_alert,name='Lalitpur_alert'),
    path('',views.register,name='register'),
    path('login/',views.loginPage,name='loginPage'),
     path('logout/',views.logoutPage,name='logoutPage'),
  
    path('oncash/<int:id>',views.cash,name='cash'),
    path('showtransactions/<int:id>',views.showtransactions,name='showtransactions'),
    path('customer_transactions/',views.customer_transactions,name='customer_transactions'),
    path('customeralert_details/<int:id>',views.customeralert_details,name='customeralert_details'),
    path('mysales/',views.mysales,name='mysales'),
     
    path('customer_details/',views.customer_details,name='customer_details'),
    path('ktm_details/<int:id>',views.ktm_details,name='ktm_details'),
    path('showcustomer/<int:id>',views.showcustomer,name='showcustomer'),
    path('Delete_kathmandu/<int:id>',views.Delete_kathmandu,name='Delete_kathmandu'),
    path('update_kathmandu/<int:id>',views.update_kathmandu,name='update_kathmandu'),
    path('Delete_bhaktapur/<int:id>',views.Delete_bhaktapur,name='Delete_bhaktapur'),
    path('update_bhaktapur/<int:id>',views.update_bhaktapur,name='update_bhaktapur'),
    path('Delete_lalitpur/<int:id>',views.Delete_lalitpur,name='Delete_lalitpur'),
    path('update_lalitpur/<int:id>',views.update_lalitpur,name='update_lalitpur'),



    
    path('salescash/',views.salescash,name='salescash'),
    
    path('kathmandu_details/',views.kathmandu_details,name='kathmandu_details'),
    path('lalitpur_details/',views.lalitpur_details,name='lalitpur_details'),
    path('bhaktapur_details/',views.bhaktapur_details,name='bhaktapur_details')
    

    

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
