class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# Change the price (This would not be changed from 900 to 1000 since it is encapsulated)
c.__maxprice = 1000
c.sell()

# Using setting function
c.setMaxPrice(1000)
c.sell()
