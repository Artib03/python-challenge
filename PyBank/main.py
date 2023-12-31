# total number for months in dataset
# net total amount of "profit/losses" over the entire period
# changes in "profit/losses" over the entire period, then the average of those changes
# the greatest increase in profits (date and amount) over the entire period
# the greatest decrease in profits (date and amount) over the entire period

import os
import csv
from tarfile import PAX_NUMBER_FIELDS

#filename = ('analysis/mytextfile.txt')

budget_data = r'PyBank\resources\budget_data.csv'

previous_row = 0
net_months = 0
total_profits = 0
month_of_change = []
net_change_list = []
greatest_increase = [",0"]
greatest_decrease = [",999999999999999999"]
total_net = 0

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
          net_change = current_profit - previous_row 
          previous_row = int(row[1]) - 0
          net_change = previous_row + 1
          total_net = net_change/ net_months
          
          #maximum_increase = max[(net_change)]
          #Wif maximum_increase == row[0] and row[2]:
               #date1 = ()
               #net_change.append(date1)

          #minimum_decrease = min[(net_change)]
          #if minimum_decrease == row[0] and row[2]
               #date2 = ()
               #net_change.append(date2)


print ("Financial Analysis")
print ("---")
print (f'Total Months: {net_months}')
print (f'Total: ${total_profits}')
print (f'average change:${total_net}')
#print (f'greatest increase in profits {maximum_increase}')
#print (f'greatest decrease in profits {minimum_decrease}')