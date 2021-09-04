import datetime
import requests
import urllib
import json

from dateutil.parser import parse

# function getTransactions(clientId) returns List
# return a list of client transactions
def getTransactions(clientId):
  #If clientId is not a number, skip parsing and return an empty list
  if (not isinstance(clientId,int)):
    return[]

  transactions = []
  dataList= [ [12345,"buy","AAPL", 10, 76.60, "2020-01-02 16:01:23"],
              [12345,"buy","AAPL", 5, 95.11, "2020-06-05 15:21:56"],
              [12345,"buy","GME", 5, 20.99, "2020-12-21 15:45:24"],
              [12345,"sell","GME", 5, 145.04, "2021-01-16 18:34:12"]
            ]

  # find matching transactions and append to list
  for data in dataList:
    if data[0] == clientId:
      transactions.append(data)
  return transactions


# function getSecurityPrice(security, target_date)
# lookup and return security price on target_date
def getSecurityPrice(security, target_date=str(datetime.datetime.now())):
  target_date=parse(target_date)

  #If this is a weekend, backup to the previous weekday, will still miss trading holidays
  this_day=target_date.weekday()
  if (this_day>4):
    this_day-=4
    target_date=target_date-datetime.timedelta(days=this_day)

  # This api only goes back 1 year for free
  api_url='http://api.marketstack.com/v1/eod'
  access_key='d77ad5c1c2cfd26c34c0b892d3974670'

  url_call="{0}?access_key={1}&symbols={3}&date_from={2}&date_to={2}".format(api_url,access_key,str(target_date.date()),security)
  req = requests.get(url_call)
  r = json.loads(req.content)
  return r['data'][0]['close']


# function portfolioOnDate(clientId, target_date=today) returns Dictionary
# parse client transactions to generate list of securities on a particular date
#  for each transaction
#   if transaction_date <= target_date, adjust quantity of security
#     if transaction_method = buy, add security
#      else, subtract security
#   if transaction_date > target_date, return portfolio
def portfolioOnDate(clientId, target_date=str(datetime.datetime.now())):
  portfolio = {}
  transactions=getTransactions(clientId)
  target_date=parse(target_date)

  for (clientId,activity,securityName,securityCount,securityPrice,transactionDate) in transactions:
    this_date=parse(transactionDate)
    if (this_date <= target_date):
      if (activity=="buy"):
        portfolio[securityName]=portfolio.get(securityName,0)+securityCount
      else:
        portfolio[securityName]=portfolio.get(securityName,0)-securityCount

  return portfolio

  


# funtion portfolioValue(portfolio, target_date) returns Long
# parse portfolio on target_date to determine value
#  for each security
#    get security_value for target_date
#    adjust total_value by security_value
#    return total_value
def portfolioValue(portfolio, target_date=str(datetime.datetime.now())):
  total_value=0

  for security in portfolio:
    security_price=getSecurityPrice(security,target_date)
    total_value+=(portfolio[security]*security_price)
  return total_value


# function getProfitLoss(clientId, start_date, end_date=today) returns Long
# determine Profit/Loss for portfolio between start_date and end_date
#  get portfolio on start_date
#  get start_value with portfolioValue
#  get portfolio on end_date
#  get end_value with portfolioValue
#  calculate final_value from start_value-end_value
#  return end_value

# routes

def main():
    partialDate="2021-01-08 01:02:03"
    now=str(datetime.datetime.now())
    #portfolio=portfolioOnDate(12345)
    portfolio=portfolioOnDate(12345,partialDate)
    print (portfolioValue(portfolio))
    portfolio=portfolioOnDate(12345)
    print (portfolioValue(portfolio))
    #print(getSecurityPrice('AAPL',"2021-01-08"))

if __name__ == "__main__":
    main()
