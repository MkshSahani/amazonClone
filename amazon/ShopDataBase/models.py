from django.db import models


# data Model sellers. 

class SellerModel(models.Model):  # Model Name : SellerModel. 
    seller_uid = models.AutoField(primary_key=True) # autincremented ID. 
    seller_name = models.CharField(max_length = 100) # seller Name. 
    seller_country = models.CharField(max_length=100) # country of seller. 
    seller_productType = models.CharField(max_length=100) # store the list in space seprated data. 
    
    def __str__(self): 
        return str(self.seller_uid) + "_" + self.seller_name + "_" + self.seller_country # return the data. 



# data Model Product. 

class Product(models.Model):  # Model Name : Product. 
    product_uid = models.IntegerField(primary_key=True) # unique ID of product. 
    product_name = models.CharField(max_length=100) # name of product. 
    seller_id = models.ForeignKey(SellerModel, related_name="Product_Seller", on_delete=models.PROTECT) # foreign key refer to seller.  
    price = models.FloatField() # price in /100 scaled. 
    

    def __str__(self): 
        return str(self.product_uid) + "_" + self.product_name # show it as label. 


# data Modle ProductReview. 

class ProductReview(models.Model): # Model Name : Prouduct Review. 
    pass 
