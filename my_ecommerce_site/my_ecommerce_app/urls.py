from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home),
    path('', views.home, name='home'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart),
    path('cart-item/', views.create_cart_item, name='create_cart_item'),
    path('cart/', views.cart),    
    path('category/<int:id>/', views.products_by_category),
    path('product/<int:id>/', views.product),
] 