 

---

#  Mohamed-Saleh_20231579_MC_Full_Stack_Python_Assessement_One

 


 

___

  


## Scope

write a plugin to check shopping kart if it has at least 5 items and value of $200 or more. if criteria is achieved a $50 discount is applied to the basket

##  Products.py 

this class handles reading and fetching products from a .csv database file using pandas.py library

## BlackfridayPlugin.py

will take as input list of products and check if the promotion criteria is applicable and return result to next part of the system to proceed with checkout. Small emulator code which generate random number of items and select random numbers from database and then passed as arguments to our Blackfridayplugin to apply promotion. 

>     blackFr=BlackfridayPlugin()
>     products = []
>     
>     for pIndex in range(1,random.randint(1,20)):
>       products.append(Products.Product.readProductFromDatabaseByIndex(random.randint(1,1000)))
>     print(blackFr.applyPromotion(products))

## pytest.py
I am using pytest.py library


>     >pytest Test_BlackfridayPlugin.py
 