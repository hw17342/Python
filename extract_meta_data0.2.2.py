import requests
import json
"""
Created on Sat May  7 18:10:51 2022
extracting the data from the json and separating from the Time Series (5min) from the Meta Data
@author: Henry

{'Meta Data': 
     {'1. Information': 'Intraday (5min) open, high, low, close prices and volume', 
      '2. Symbol': 'IBM', 
      '3. Last Refreshed': '2022-05-06 20:00:00', 
      '4. Interval': '5min', 
      '5. Output Size': 'Compact', 
      '6. Time Zone': 'US/Eastern'},
     
 'Time Series (5min)': 
     {'2022-05-06 20:00:00': 
         {
         '1. open': '137.6700', 
         '2. high': '137.6700', 
         '3. low': '137.6700', 
         '4. close': '137.6700', 
         '5. volume': '103'}
"""
# API request getting TIME_SERIES_INTRADAY in a JSON file
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=FEO9OIDK662UC6NO'
r = requests.get(url)
json_data = r.json()

#The following all print the data at different levels of details
# print((json_data['Meta Data']))
# print((json_data['Time Series (5min)']))
# print((json_data['Meta Data']['2. Symbol']))
# print((json_data['Time Series (5min)']['2022-05-06 20:00:00']))
print((json_data['Time Series (5min)']['2022-05-06 20:00:00']['1. open']))

