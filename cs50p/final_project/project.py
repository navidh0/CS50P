
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator
from datetime import datetime


'''
The class trend uses yahoo finance library to fetch "Gold" data
uses SMA Indicator {SMA : Simple Moving Average} detemine the trend of market
pandas library to store the data in csv
and matplotlib to visualize

Note : this class can be modified to use alphavantage as endpoint with api_key
Symbol of the class can be changed to analyze other stocks but by default is set to Gold


'''
class Trend:
    def __init__(self, symbol= 'GLD'):
        self.symbol =symbol
        self.data= None

    def date_checker(self, start_date = None ,end_date = None):
            try:
                self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
                self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
                days = (self.end_date - self.start_date).days
                if  days >= 30:
                    self.window = days
                else:
                    return "Minimum 30 days is required. Please try again"
            except ValueError:
                return 'Invalid Date Format. Please try again'
            return None
                

    def get_data(self):
        data = yf.download(self.symbol, start= self.start_date , end= self.end_date)
        self.data = data

    def store(self, filename = "Gold.csv"):
        if self.data is not None:
            self.data.to_csv(filename, index= False)
            print("Data has been stored")
        else:
            print("No data, Please use the get_data method first ")

    def analyze(self):
        if self.data is not None:
            sma = SMAIndicator(self.data['Close'], window = self.window)
            plt.figure(figsize=(12,6))
            plt.plot(self.data['Close'], label='Close Price')
            plt.title(f"{self.symbol} in {self.window} days SMA")
            plt.plot(sma.sma_indicator(), label=f"{self.window}-day SMA", color = "blue")
            plt.xlabel('Date')
            plt.ylabel("Price")
            plt.xticks(rotation = 45)
            plt.legend()
            plt.show()
        else:
            print("No data, Please use the get_data method first ")


def main():
    while True:
        try:
            start= input("Enter Start Date (YYYY-MM-DD): ")
            end= input("Enter End Date (YYYY-MM-DD): ")
            stock = Trend()
            stock.date_checker(start_date=start , end_date=end)
            break
        except Exception:
            pass
    stock.get_data()
    stock.store()
    stock.analyze()

if __name__ =="__main__":
    main()
