# function getTransactions(clientId) returns List
# return a list of client transactions

# function portfolioOnDate(clientId, target_date=today) returns Dictionary
# parse client transactions to generate list of securities on a particular date
#  for each transaction
#   if transaction_date <= target_date, adjust quantity of security
#     if transaction_method = buy, add security
      else, subtract security
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
