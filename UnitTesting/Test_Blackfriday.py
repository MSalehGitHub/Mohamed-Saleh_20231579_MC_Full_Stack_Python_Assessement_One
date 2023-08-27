import pytest
import BlackfridayPlugin
import Products



class TestBlackfridayPlugin:

    productsdb = Products.Product
    blackFr=BlackfridayPlugin()

    def test_plugin_promotion1(self):
        basket=[]
        for i in range(1,7,1):# products from index 1 to 7
            basket.append(Products.Product.readProductFromDatabaseByIndex(i))
        assert( self.blackFr.applyPromotion(basket)[0]==True)
