#testing if stock works
from StockModule import Stock
def main():
    symbol= eval(raw_input("Enter in a symbol for the stock company(in quotations):" ))
    name= eval(raw_input("Enter in a name for the stock company(in quotations): "))
    currentPrice = eval(raw_input("Enter in a value for the current price of the stock(as a float): "))
    PreviousClosingPrice= eval(raw_input("Enter in a value for the previous closing price(as a float): "))
    stock= Stock(PreviousClosingPrice, currentPrice, name, symbol)
    print("The symbol of the stock company is", stock.getSymbol())
    print("The name of the stock company is ", stock.getName())
    print("The percent change is ", format(stock.getChangePercent(), ".2f"))
    
    
main()
    
    