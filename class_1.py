class customer:
    name = ""
    age = 0
    last_name = ""
    
    def addcart(self):
        print("Added to cart",self.last_name,self.name,"s cart")


customer1 = customer()
customer1.last_name = "Peach"
customer1.name = "inc"
customer1.addcart()

customer2 = customer()
customer2.last_name = "Punch"
customer2.name = "inc"
customer2.addcart()

customer2 = customer()
customer2.last_name = "tanat"
customer2.name = "inc"
customer2.addcart()

customer2 = customer()
customer2.last_name = "wan"
customer2.name = "as"
customer2.addcart()