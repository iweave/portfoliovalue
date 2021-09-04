# function getTransactions(clientId) returns List
# return a list of client transactions
def getTransactions(clientId):
  #If clientId is not a number, skip parsing and return an empty list
  if (not isinstance(clientId,int)):
    return[]

  transactions = []
  dataList= [ [12345,"buy","APPL", 10, 76.60, "2020-01-02 16:01:23"],
              [12345,"buy","APPL", 5, 95.11, "2020-06-05 15:21:65"],
              [12345,"buy","GME", 5, 20.99, "2020-12-21 15:45:24"],
              [12345,"sell","GME", 5, 145.04, "2021-01-06 18:34:12"]
            ]

  # find matching transactions and append to list
  for data in dataList:
    if data[0] == clientId:
      transactions.append(data)
  return transactions



# function portfolioOnDate(clientId, target_date=today) returns Dictionary
# parse client transactions to generate list of securities on a particular date
#  for each transaction
#   if transaction_date <= target_date, adjust quantity of security
#     if transaction_method = buy, add security
#      else, subtract security
#   if transaction_date > target_date, return portfolio

# funtion portfolioValue(portfolio, target_date) returns Long
# parse portfolio on target_date to determine value
#  for each security
#    get security_value for target_date
#    adjust total_value by security_value
#    return total_value

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
    print(getTransactions(12345))

if __name__ == "__main__":
    main()
