from django.shortcuts import redirect,render
from django.contrib import messages
from django.http.response import JsonResponse
from .models import *
def addtocart(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=product.objects.get(id=prod_id)
            if (product_check):
                if(cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status': "produit déjà dans le panier"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity>=prod_qty:
                        cart.objects.create(user=request.user, product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status': "produit ajouté avec succès"})
                    if product_check.quantity == 0:
                        return JsonResponse({'status': "stock epuise"})
                    else:
                         return JsonResponse({'status': "seulment "+str(product_check.quantity)+" Quantité disponible"})
            else:
                return JsonResponse({'status':"aucun produit de ce type trouvé"})
        else:
            return JsonResponse({'status': "connectez-vous pour continuer"})
    return redirect('/')

def viewcart(request):
    Cart=cart.objects.filter(user=request.user)
    context={'cart':Cart}
    return render(request,"users/cart.html",context)
def updatecart(request):
    if request.method=="POST":

            prod_id=int(request.POST.get('product_id'))
            if(cart.objects.filter(user=request.user,product_id=prod_id)):

              prod_qty=int(request.POST.get('product_qty'))
              Cart=cart.objects.get(user=request.user,product_id=prod_id)
              Cart.product_qty=prod_qty
              Cart.save()
              return JsonResponse({'status':"Mis à jour avec succès"})
    return redirect('/')
def deletecartitem(request):
    if request.method=="POST":

            prod_id=int(request.POST.get('product_id'))
            if(cart.objects.filter(user=request.user,product_id=prod_id)):


              Cartitem=cart.objects.get(user=request.user,product_id=prod_id)

              Cartitem.delete()
              return JsonResponse({'status':"supprimé avec succès"})
    return redirect('/')