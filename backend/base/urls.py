from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .models import *
from . import cart,checkout
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('product/', views.acces, name='product'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('car/<int:pk>', views.car, name='car'),
    path('voiture/', views.voiture, name='voiture'),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('add-to-cart',cart.addtocart,name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('checkout',checkout.index,name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),

]
