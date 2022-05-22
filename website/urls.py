from django.urls import path,include
from website import views

urlpatterns = [
    path('home',views.home),
    path('products',views.products),
    path('about',views.about),
    path('garmets',views.garmets),
    path('lights',views.lights),
    path('search',views.search),
    path('products/<str:ext>',views.prod),
]