from django.db import models


# data Model sellers. 

class SellerModel(models.Model):  # Model Name : SellerModel. 
    seller_uid = models.AutoField(primary_key=True) # autincremented ID. 
    seller_name = models.CharField(max_length = 100) # seller Name. 
    seller_country = models.CharField(max_length=100) # country of seller. 
    seller_productType = models.CharField(max_length=100) # store the list in space seprated data. 
    
    def __str__(self): 
        return str(self.seller_uid) + "_" + self.seller_name + "_" + self.seller_country # return the data. 