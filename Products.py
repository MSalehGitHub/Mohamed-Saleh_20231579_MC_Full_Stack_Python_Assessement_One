import pandas as pd
from decimal import Decimal
from re import sub

class Product:

    ProductsDB = pd.read_csv('DataFiles\\amazon_co-ecommerce_sample.csv'); 

    currentRecordIndex=0

    def __init__(self,_id,_price,_name) -> None:
        self.id=_id
        self.name=_name
        self.price=_price

   

    @classmethod
    def readProductFromDatabase(self ):
       
         
        record =  Product.ProductsDB.iloc[Product.currentRecordIndex]
        Product.currentRecordIndex+=1
        if(len(Product.ProductsDB) ==  Product.currentRecordIndex):
            Product.currentRecordIndex=0
         

        p=Product(_id=record['uniq_id'],_name=record['product_name'],_price=Decimal(sub(r'[^\d.]', '',record['price'])) )
        return p
    
    @classmethod
    def readProductFromDatabaseByIndex(self,recordIndex ):
       
        if(recordIndex>=0 and recordIndex < len(Product.ProductsDB)):
            record =  Product.ProductsDB.iloc[recordIndex] 
            p=Product(_id=record['uniq_id'],_name=record['product_name'],_price=record['price'])
            return p
    


