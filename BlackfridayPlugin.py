import Products

class BlackfridayPlugin:

    DiscountAmount = 50
    DiscountPercentage = 0.2


    def __init__(self) -> None:
        pass

    #dynamic function thats accept promotion related params and check if it applies and return the value
    #our criteria in this assignement is (NumberOfItems>=5 and TotalAmount>=USD200)
    def promotionCriteria(self,**kwargs):
        if(kwargs['NumItem'] >=5 and kwargs['TotalAmount']>=200.0):
            return True
        
        return False
    
    def calculateShoppingCartTotalAmount(self,productsList ):

        totalAmount=0
        for p in productsList:
            
            totalAmount = totalAmount + p.price
        pass
        
       # print(f"Total => {totalAmount}")
        return totalAmount
#################################


    def applyPromotion(self,productsList):
        numItems = len(productsList)
        shoppingCartTotal = self.calculateShoppingCartTotalAmount(productsList)

        if( self.promotionCriteria(NumItem=numItems,TotalAmount=shoppingCartTotal)  ):
            newPriceAfterDiscount = shoppingCartTotal - self.DiscountAmount
            
            return (True,f"Congratulations Promotion applied  ",numItems,round((shoppingCartTotal*100)/100,2),round((newPriceAfterDiscount*100)/100,2))
        else:
            newPriceAfterDiscount = shoppingCartTotal
             
            return (False,f"Sorry Try Later  ",numItems,round((shoppingCartTotal*100)/100,2),round((newPriceAfterDiscount*100)/100,2))

######################################################################

# product=[Products.Product.readProductFromDatabase(),
#          Products.Product.readProductFromDatabase(),
#          Products.Product.readProductFromDatabase(),
        
#          Products.Product.readProductFromDatabase(),
#          Products.Product.readProductFromDatabase()         
#          ]


# product=[Products.Product.readProductFromDatabaseByIndex(10),
#          Products.Product.readProductFromDatabaseByIndex(20),
#          Products.Product.readProductFromDatabaseByIndex(30),
#          Products.Product.readProductFromDatabaseByIndex(40)        
         
#          ]



product=[Products.Product.readProductFromDatabaseByIndex(100),
         Products.Product.readProductFromDatabaseByIndex(200),
         Products.Product.readProductFromDatabaseByIndex(300),
         Products.Product.readProductFromDatabaseByIndex(400),        
         Products.Product.readProductFromDatabaseByIndex(500)        
         
         ]

blackFr=BlackfridayPlugin()

print(blackFr.applyPromotion(product))
