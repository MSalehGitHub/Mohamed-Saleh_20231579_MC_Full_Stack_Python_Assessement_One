import pandas as pd


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
         

        p=Product(_id=record['uniq_id'],_name=record['product_name'],_price=record['price'])
        return p
    




while (True):
    x= Product.readProductFromDatabase()
    print(f'[{Product.currentRecordIndex}] {x.id} , {x.name} , {x.price}')
    

