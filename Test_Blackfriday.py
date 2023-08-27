
from  BlackfridayPlugin import *
from  Products import *
import pytest


class Test_BlackfridayPlugin:
    pass
    
    blackFr=BlackfridayPlugin()

    def test_plugin_promotion1(self):
        basket=[]
        for i in range(1,8,1):# products from index 1 to 7
            basket.append(Products.Product.readProductFromDatabaseByIndex(i))
       
        assert( self.blackFr.applyPromotion(basket)[0]==True)

    def test_plugin_promotion2(self):
        basket=[]
        for i in range(10,41,10):# products from index 10 to 40
            basket.append(Products.Product.readProductFromDatabaseByIndex(i))
       
        assert( self.blackFr.applyPromotion(basket)[0]==False)

    def test_plugin_promotion3(self):
        basket=[]
        for i in range(100,501,100):# products from index 10 to 40
            basket.append(Products.Product.readProductFromDatabaseByIndex(i))
       
        assert( self.blackFr.applyPromotion(basket)[0]==False)