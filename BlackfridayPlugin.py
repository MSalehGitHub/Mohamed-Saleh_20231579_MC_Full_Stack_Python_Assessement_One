import Products

class BlackfridayPlugin:

    DiscountAmount = 50
    DiscountPercentage = 0.2

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


    def applyPromotion(self,productsList):
        numItems = len(productsList)
        shoppingCartTotal = self.calculateShoppingCartTotalAmount(productsList)

        if( self.promotionCriteria(NumItem=numItems,TotalAmount=shoppingCartTotal)  ):
            newPriceAfterDiscount = shoppingCartTotal - self.DiscountAmount
            
            return (f"Congratulations Promotion applied  ",numItems,shoppingCartTotal,newPriceAfterDiscount)
        else:
            newPriceAfterDiscount = shoppingCartTotal
             
            return (f"Sorry Try Later  ",numItems,shoppingCartTotal,newPriceAfterDiscount)

######################################################################

product=[Products.Product.readProductFromDatabase(),
         Products.Product.readProductFromDatabase(),
         Products.Product.readProductFromDatabase(),
         Products.Product.readProductFromDatabase()         
         ]
blackFr=BlackfridayPlugin()

blackFr.calculateShoppingCartTotalAmount(product)