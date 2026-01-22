class computer:

    def __init__(self):
        self.__maxsprice = 900
    
    def sell(self):
        print("Selling price {}".format(self.__maxsprice))
    
    def setmaxsprice(self, price):
        self.__maxsprice = price

c = computer()
c.sell()

c.__maxsprice = 1000
c.sell()

c.setmaxsprice(1000)
c.sell()