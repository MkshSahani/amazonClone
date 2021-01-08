from django.contrib import admin
from .models import SellerModel, Product

admin.site.register(SellerModel) # register Seller Model. 
admin.site.register(Product) # register product Model. 