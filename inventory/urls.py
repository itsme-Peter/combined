from django.urls import path,include
from inventory import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('stocks',views.stocks),
    path('order',views.order),
    path('users',views.users),
    path('edit_stock/<str:id>',views.edit),
    path('logout',views.log_out),
    path('sign',views.sign),
]