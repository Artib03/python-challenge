# total number for months in dataset
# net total amount of "profit/losses" over the entire period
# changes in "profit/losses" over the entire period, then the average of those changes
# the greatest increase in profits (date and amount) over the entire period
# the greatest decrease in profits (date and amount) over the entire period

import os
import csv

Month_IND = 0
Profit_IND = 1

budget_data = r'PyBank\resources\budget_data.csv'
net_months = 0
total_profits = 0
prev_row = None

with open(budget_data, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvfile)

     for row in csvreader:
          #total months
          net_months = net_months + 1
          
          #total profits
          current_profit = int(row[1])
          total_profits = current_profit + total_profits

     # ---changes and average of changes
     current_row = int(row[1])
if prev_row is not None:
     change = current_row - prev_row
     current_row = prev_row
     average_change = change / 86


#values = int(input('what are the maximum and minimum values?'))

     #greatest increase in profits
if row in csvreader:
     float(row[1]) == max(row[1]):
     print (row)
     elif
     int(row [1]) = min(row[1]):
     float(row)

     #date of greatest increase in profits
     

     #greatest decrease in profits 
    

     #date of greatest decrease
     
print ("Financial Analysis")
print ("---")
print (f'Total Months: {net_months}')
print (f'Total: {total_profits}')
#print (f'{}')



#class 3 activity 7 (refer to)

#main.py = 'Analysis/mytextfile.txt'

