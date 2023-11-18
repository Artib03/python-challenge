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
     #net_change = int(row[1]) - previous_row
     #previous_row = int(row[1])
     #net_change_list += [net_change]
     #month_of_change += [row[0]

     #greatest increase in profits + date
#def maximum (max_num):
     #for max_num in max_num:
          #max_num = int(row[1])
     #return maximum

#greatest decrease in profits + date
#def minimum (min_num):
     #for min_num in min_num:
         #min_num = int(row[1])
     #return minimum 
     
print ("Financial Analysis")
print ("---")
print (f'Total Months: {net_months}')
print (f'Total: {total_profits}')
#print (f'average change:{changes}')
#print (f'greatest increase in profits{maximum}')
#print (f'greatest decrease in profits{minimum}')

#class 3 activity 7 (refer to)