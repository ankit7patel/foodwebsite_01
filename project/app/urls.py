from django.urls import path
from app import views

urlpatterns = [
    path('',views.home , name='home'),
    path('about/',views.about , name='about'),
    path('gallery/',views.gallery , name='gallery'),
    path('menu/',views.menu , name='menu'),
    path('order/',views.order , name='order'),
    path('review/',views.review , name='review'),
    path('register/',views.register , name='register'),
    path('login/',views.login , name='login'),
    path('query/',views.query,name='query'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/new/', views.order, name='order'),
    path('orders/edit/<int:pk>/', views.order_update, name='order_update'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),
     path('logout/',views.logout , name='logout')


]