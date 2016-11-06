#Stock class, design a class named stock to represent a company's stock
#a private string data field name symbol for the stock's symbol
# a private string named name for the stock's name
#a private float named previousClosingPrice that stores the closing price for the previous dayu.
# a prive float data field named currentPrice that stores the stock for the current time
#a constructor that creates a stock with the specified symbol, name, previous price and current price
#a  get method for returning the stock name
#a get method for returning the stock symbol
#Get and set methods for getting/setting the stock previous price
# a get and set methods for stocks current price
#A method named getChangePercent() that returnss the percent changed from previous Closing to current price
#let's define the class first
class Stock(object):
    def __init__(self, previousClosingPrice, currentPrice, symbol= " " , name= " " ,):
        self.__symbol = symbol
        self.__name= name
        self.__previousClosingPrice= previousClosingPrice
        self.__currentPrice= currentPrice
    #creaation of the get methods for name and symbol
    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    #creation of the get method for stock previous price
    def getPreviousPrice(self):
        return self.__previousClosingPrice
    def getCurrentPrice(self):
        return self.__currentPrice
    #now do the set methods 
    def setPreviousPrice(self, previousClosingPrice):
        self.__previousClosingPrice= previousClosingPrice
    #set with the current price
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice= currentPrice
    #method for change percent
    def getChangePercent(self):
        increase= self.__currentPrice- self.__previousClosingPrice
        percentnow= (increase / self.__previousClosingPrice) * 100
        return percentnow
    
    
    