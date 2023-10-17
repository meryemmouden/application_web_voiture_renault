from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(product)
admin.site.register(accessoir)
admin.site.register(cart)
admin.site.register(order)
admin.site.register(orderItem)
admin.site.register(profile)