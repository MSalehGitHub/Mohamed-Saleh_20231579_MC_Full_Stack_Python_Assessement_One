import pandas as pd
from decimal import Decimal
from re import sub
import math

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
        
        recId = record['uniq_id']
        recName = record['product_name']
        recPrice = 0.0
        try:
          recPrice =   float(record['price'])
        except ValueError:
            recPrice = float(sub(r'[^\d.]+','',record['price']))

        if( math.isnan(recPrice)):
            recPrice = 0


        p=Product(_id=recId,_name=recName,_price=recPrice )
        return p
    
    @classmethod
    def readProductFromDatabaseByIndex(self,recordIndex ):
       
        if(recordIndex>=0 and recordIndex < len(Product.ProductsDB)):
            record =  Product.ProductsDB.iloc[recordIndex]        
            
            recId = record['uniq_id']
            recName = record['product_name']
            recPrice = 0.0
            try:
                 recPrice =   float(record['price'])
            except ValueError:
                recPrice = float(sub(r'[^\d.]+','',record['price']))

            if( math.isnan(recPrice)):
                recPrice = 0


            p=Product(_id=recId,_name=recName,_price=recPrice )
            return p
    


