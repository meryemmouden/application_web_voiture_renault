from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponse
import random




from django.contrib.auth.models import User
def index(request):
    rawcart=cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
           c=cart.objects.get(id=item.id)
           c.delete()
    cartitems = cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price=total_price + item.product.selling_price * item.product_qty
    userprofile=profile.objects.filter(user=request.user).first()
    context={'cartitems':cartitems,'total_price':total_price,'userprofile':userprofile}
    return render(request,'users/checkout.html',context)

def placeorder(request):
    if request.method=="POST":
        currentuser=User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('fname')
            currentuser.last_name=request.POST.get('lname')
            currentuser.save()
        if not profile.objects.filter(user=request.user):
            userprofile=profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.adress = request.POST.get('adress')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()

        neworder=order()
        neworder.user=request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname =  request.POST.get('lname')
        neworder.email =  request.POST.get('email')
        neworder.phone =  request.POST.get('phone')
        neworder.adress =  request.POST.get('adress')
        neworder.city =  request.POST.get('city')
        neworder.state =  request.POST.get('state')
        neworder.country=  request.POST.get('country')
        neworder.pincode=  request.POST.get('pincode')
        neworder.payment_mode = request.POST.get('payment_mode')

        Cart=cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in Cart:
          cart_total_price=cart_total_price+item.product.selling_price*item.product_qty

        neworder.total_price=cart_total_price
        trackno='sharma'+str(random.randint(1111111,9999999))
        while order.objects.filter(tracking_no=trackno) is None:
           trackno = 'sharma' + str(random.randint(1111111, 9999999))

        neworder.tracking_no=trackno
        neworder.save()

        neworderitems=cart.objects.filter(user=request.user)
        for item in neworderitems:
           orderItem.objects.create(
                    Order=neworder,
                    product=item.product,
                    price=item.product.selling_price,
                    quantity=item.product_qty
           )
           orderproduct=product.objects.filter(id=item.product_id).first()
           orderproduct.quantity=orderproduct.quantity-item.product_qty
           orderproduct.save()

        cart.objects.filter(user=request.user).delete()
        messages.success(request,"votre commande a été passée avec succès")
    return redirect('/checkout')


